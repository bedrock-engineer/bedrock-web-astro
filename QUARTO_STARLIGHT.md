# Custom Quarto Starlight Format

This document outlines research into creating a custom Quarto format for Starlight compatibility.

## Problem

Quarto's built-in formats don't handle callouts in a way that's compatible with Astro/Starlight. Specifically:

- `commonmark` format converts callouts to blockquotes with `> **Note**` syntax
- `docusaurus-md` format correctly converts to `:::note` but includes React-specific elements. Astro doesn't use React to render inline HTML in MDX files.
- Starlight expects `:::note` / `:::tip` / `:::caution` syntax

## Current Working Solution

We use `commonmark` format with Python post-processing:

```yaml
# _quarto.yml
format:
  commonmark:
    embed-resources: true
    template: starlight-template.md
post-render:
  - "uv run python fix-callouts.py src/content/docs/examples/quarto.md"
```

The `fix-callouts.py` script converts blockquote callouts to Starlight syntax using regex.

## Research into Custom Format

### Quarto Extension Structure

Attempted to create a custom format extension:

```
_extensions/starlight-md/
├── _extension.yml
└── starlight-callouts.lua
```

**_extension.yml:**
```yaml
title: Starlight Markdown
author: Bedrock
version: 1.0.0
quarto-required: ">=1.4.0"
contributes:
  formats:
    starlight-md:
      extends: commonmark
      embed-resources: true
      template: ../../../../starlight-template.md
      filters:
        - starlight-callouts.lua
```

### Why Custom Renderer Approach Failed

1. **Early Processing**: Quarto processes callouts in the parse phase, before user Lua filters run
2. **Internal APIs**: The `_quarto.ast.add_renderer("Callout", ...)` API is internal and not available to user extensions
3. **Format Coupling**: Callout rendering is tightly coupled to specific output formats

### Evidence from Quarto Source

Found this in `docusaurus_renderers.lua`:

```lua
_quarto.ast.add_renderer("Callout", function()
  return we_are_docusaurus -- detect docusaurus-md
end, function(node)
  local admonition = pandoc.List()
  admonition:insert(pandoc.RawBlock("markdown", "\n:::" .. node.type))
  if node.title then
    admonition:insert(pandoc.Header(2, node.title))
  end
  local content = node.content
  if type(content) == "table" then
    admonition:extend(content)
  else
    admonition:insert(content)
  end
  admonition:insert(pandoc.RawBlock("markdown", ":::\n"))
  return admonition
end)
```

This shows exactly what we need, but the `_quarto.ast.add_renderer` API is not exposed to user extensions.

### Failed Approaches

1. **Lua Filter with Div Processing**: Callouts are already converted to HTML divs before filters see them
2. **Custom Extension**: Extension system works but can't access internal renderer APIs
3. **RawBlock Processing**: Callouts are processed too early in the pipeline

### Limitations of Quarto's Architecture

- Callout processing happens before user filters can intercept
- Internal APIs are not exposed for stability reasons
- Format-specific logic is not easily extensible
- Extension documentation is incomplete for advanced use cases

## Future Possibilities

### Ideal Solution

A proper `starlight-md` format that:
- Inherits from `commonmark`
- Uses Quarto's internal callout renderer with Starlight mappings
- Handles frontmatter properly
- Preserves inline HTML

### Potential Approaches

1. **Contribute to Quarto**: Submit PR to add `starlight-md` as built-in format
2. **Extension with Custom Writer**: Create a custom Pandoc writer for Starlight
3. **Fork Quarto**: Modify Quarto source to expose renderer APIs
4. **Wait for API**: Hope Quarto exposes renderer APIs in future versions

### What This Would Look Like

If the internal APIs were exposed, the extension would work like this:

```lua
-- In starlight-callouts.lua
_quarto.ast.add_renderer("Callout", function()
  return true -- always use for starlight-md format
end, function(node)
  local type_mapping = {
    ["note"] = "note",
    ["tip"] = "tip", 
    ["warning"] = "caution",
    ["caution"] = "caution",
    ["important"] = "note",
    ["danger"] = "danger"
  }
  
  local starlight_type = type_mapping[node.type] or "note"
  
  local result = pandoc.List()
  result:insert(pandoc.RawBlock("markdown", ":::" .. starlight_type))
  
  if node.title then
    result:insert(pandoc.Header(2, node.title))
  end
  
  result:extend(node.content)
  result:insert(pandoc.RawBlock("markdown", ":::"))
  
  return result
end)
```

## Conclusion

While Quarto does support custom formats through extensions, the specific functionality needed for Starlight callouts requires access to internal APIs that aren't exposed. 

The Python post-processing approach is actually more reliable and maintainable than trying to work around these limitations. It's a common pattern in the Quarto ecosystem for handling format-specific customizations.

**Recommendation**: Stick with the current Python post-processing solution until Quarto either:
1. Exposes the renderer APIs publicly
2. Adds built-in Starlight support
3. Improves the extension system for this use case