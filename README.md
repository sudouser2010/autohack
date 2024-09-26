# Auto Hack
* note the setup steps described here are being beta-tested.

## This package does automated vulnerability enumeration and recommends exploits.<br><br>

### How to Run on Non Kali-Linux Operating System (Recommended)

* Create AutoHack Docker container
  ```
  docker run -ti -v ${PWD}/portal:/root/portal hdizzle/autohack 
  ```
  Command above does the following:
  * creates Docker container based on the [AutoHack image](https://registry.hub.docker.com/r/hdizzle/autohack)
  * mounts a folder named `portal` in current directory
    * this allows us to persists the AutoHack results once the <br>container is destroyed
  * allows us to access the terminal of the AutoHack container

* Run AutoHack

  ```
  autohack -i <some ip address>
  ```
  
---  

### How to Run on Kali-Linux Operating System
* Install AutoHack Python Package

    ```
    pip install autohack
    ```
* Run AutoHack
  ```
  autohack -i <some ip address>
  ```