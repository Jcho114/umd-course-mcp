# UMD Course MCP Server

API wrappers over [PlanetTerp](https://planetterp.com/) and [UMDIO](https://beta.umd.io/) that lets LLMs make more up to date and informed decisions on all things UMD, at least academically.

## How To Use

You can test in Claude Desktop using this [tutorial](https://modelcontextprotocol.io/quickstart/server#testing-your-server-with-claude-for-desktop) and it doesn't take that long.

## Caveat

Since I only really wrapped over existing APIs there are some annoying unoptimal issues with specific use cases. For example, if you ask questions regarding a specific professor, but do not provide a full name, Claude will first fail to find your professor, then query for all professors, then maybe even query for all professors for a course if possible.

I will probably find ways to narrow down the fleet of tools and maybe add some helper code to do some of this stuff under the hood without requiring multiple tool calls.

## What I Learned

This is lowkey not a real project lol. It is cool, but there is barely anything about it that made me feel proud. Maybe that can change when I start doing more than just wrap apis. Have fun with it, though.