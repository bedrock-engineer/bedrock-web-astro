// @ts-check
import { rehypeHeadingIds } from "@astrojs/markdown-remark";
import mdx from "@astrojs/mdx";
import react from "@astrojs/react";
import starlight from "@astrojs/starlight";
import tailwindcss from "@tailwindcss/vite";
import { defineConfig } from "astro/config";
import remarkDefinitionList from "remark-definition-list";
import starlightLinksValidator from "starlight-links-validator";

// https://astro.build/config
export default defineConfig({
  site: "https://bedrock.engineer",
  integrations: [
    starlight({
      plugins: [starlightLinksValidator()],
      title: "Bedrock",
      customCss: [
        // Relative path to your custom CSS file
        "./src/styles/custom.css",
      ],
      lastUpdated: true,
      logo: {
        light: "/src/assets/bedrock.svg",
        dark: "/src/assets/bedrock.svg",
        replacesTitle: true,
      },
      favicon: "/src/assets/bedrock.svg",
      editLink: {
        baseUrl:
          "https://github.com/bedrock-enginer/bedrock-web/edit/main/docs/",
      },
      social: [
        {
          icon: "github",
          label: "GitHub",
          href: "https://github.com/bedrock-engineer/bedrock-ge/",
        },
        {
          icon: "linkedin",
          label: "LinkedIn",
          href: "https://www.linkedin.com/company/bedrock-engineer/",
        },
      ],
      sidebar: [
        {
          label: "Start Here",
          items: [
            "getting-started",
            // "manual-setup"
          ],
        },
        {
          label: "Explanation",
          autogenerate: { directory: "explanation" },
        },
        {
          label: "Guides",
          autogenerate: { directory: "guides" },

          // items: [
          //   // Each item here is one entry in the navigation menu.
          //   { label: "Example Guide", slug: "guides/example" },
          // ],
        },
        {
          label: "Examples",
          autogenerate: { directory: "examples" },
        },

        {
          label: "Reference",
          autogenerate: { directory: "reference" },
        },
        {
          label: "Resources",
          items: [
            { label: "About", slug: "about" },
            { label: "Professional support", slug: "professional-support" },
          ],
        },
      ],
    }),
    mdx({
      optimize: true,
    }),
    react({ experimentalReactChildren: true }),
  ],
  markdown: {
    rehypePlugins: [rehypeHeadingIds],
    remarkPlugins: [remarkDefinitionList],
  },
  vite: {
    plugins: [tailwindcss()],
  },
});
