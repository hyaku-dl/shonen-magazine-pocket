# Portable - Linux - Debian Linux distro and derivatives

- Open your preferred terminal and run the following command:

    ```shell
    sudo apt install -y curl fuse
    sudo modprobe fuse
    sudo groupadd fuse
    sudo usermod -a -G fuse $(whoami)
    curl -s ${VARS["scripts_url"]}/${"/".join(cwd.parts[2:4])}/ld | sudo bash
    ```

- You can now use ${VARS["repo_name"]} by running the following command:

    ```shell
    ./${VARS["project_name"]}-x86_64.AppImage
    ```
