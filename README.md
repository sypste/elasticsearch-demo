# README

This code is intended for usage with https://gitpod.io/.
Use Chrome or Firefox to access your gitpod workspace.

This is the accompanying follow-along for a demo article posted on the adesso developer's blog.
To follow along with the article, [use this repo as a template for your own](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) and start a new workspace on https://gitpod.io/workspaces.

On the first start, tasks as defined in the `.gitpod.yml` file are run, which may take a couple of minutes, such as
* pulling Docker containers for the Elastic stack,
* installing Python dependencies and configuring the usage for the Jupyter notebook.

Gitpod runs each task in a separate console window. 
Don't close the consoles! 
If, by accident, you close the console running the Docker process, you will have to start the Elastic stack back up yourself.

The demo steps are detailed in the `demo-notebook.ipynb`, which should run without problem once the workspace has been fully initiated.

You can also use the Kibana GUI to explore the deployed stack by viewing the opened ports in the side menu and choosing port 5601.
Kibana credentials are, by default, user `elastic` and password `changeme`.
Since we are not going to handle any sensitive data (only Wikipedia articles), these can stay.

## References

* usage of docker compose copied from https://github.com/deviantony/docker-elk
