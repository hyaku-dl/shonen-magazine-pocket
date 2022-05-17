# Programmatic - Linux - Debian linux distro and derivatives

- Open your preferred terminal and run the following command:

    ```shell
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)
    ```

- Next, for OS X 10.13 (High Sierra) or younger, run the following command:

    ```shell
    echo 'export PATH="/usr/local/opt/python/libexec/bin:$PATH"' >> ~/.profile
    ```

    For OS X 10.12 (Sierra) or older, use the following command instead:

    ```shell
    echo 'export PATH=/usr/local/bin:/usr/local/sbin:$PATH' >> ~/.profile
    ```

- Afterwards, install the rest of the prerequisites by running the following command:

    ```shell
    brew install python
    ```

- Then, install shonen-magazine-pocket in your python installation by running the following command:

    ```shell
    python3 -m pip install shonen-magazine-pocket
    ```

- You can now use shonen-magazine-pocket programmatically!
