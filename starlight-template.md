---
title: "$title$"
description: "$description$"
$if(sidebar.order)$
sidebar:
  order: $sidebar.order$
$endif$
$if(sidebar.label)$
sidebar:
  label: "$sidebar.label$"
$endif$
$if(draft)$
draft: $draft$
$endif$
$if(lastUpdated)$
lastUpdated: $lastUpdated$
$endif$
$if(prev)$
prev: $prev$
$endif$
$if(next)$
next: $next$
$endif$
$if(editUrl)$
editUrl: $editUrl$
$endif$
$if(head)$
head: $head$
$endif$
$if(tableOfContents)$
tableOfContents: $tableOfContents$
$endif$
$if(banner)$
banner: $banner$
$endif$
---

$body$