A **Databricks App** is a way to host a small web application directly inside your Databricks workspace, running on Databricks-managed compute.

The essentials:

- **What it is:** a long-running web server (Python or Node) that Databricks deploys, runs, health-checks, and exposes at a URL — you provide the code plus a config file (`app.yaml`) and a dependency list.
- **What it requires:** just that your process listens on the assigned port and answers HTTP. It can serve a UI, a REST/JSON API, an MCP server, or anything else. A front-end is optional.
- **Why use it:** it runs *inside* the Databricks security and identity boundary, so it can reach Unity Catalog, SQL warehouses, Lakebase, secrets, and other workspace resources using governed access, without you standing up separate infrastructure.
- **Common frameworks:** Flask, FastAPI, Dash, Streamlit, Gradio, and similar.
- **Typical uses:** internal dashboards, data-entry and admin tools, ML/LLM demo front-ends, and lightweight APIs or agent tool servers that sit close to your data.

In one line: it's Databricks' built-in platform for deploying and hosting web services next to your data, with governed access to workspace resources — UI or not.