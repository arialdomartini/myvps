set -e
set -u

SERVER=37.247.55.31
USER=$LOGNAME

red="\033[0;31m"
green="\033[0;32m"
yellow="\033[0;33m"
violet="\033[0;35m"
reset="\033[0m"

function msg() {
    message=$1
    echo "${green}${message}${reset}"
}

function log() {
    msg "> ${1}"
}

function execute_remotely() {
    ssh root@${SERVER} $1
}

log "Setting permissions on remote server authorizing ${USER}'s ssh key"
cat ~/.ssh/id_rsa.pub | execute_remotely "mkdir -p ~/.ssh; cat > ~/.ssh/authorized_keys"

log "Installing the essential software to run Fabric"
execute_remotely "apt-get update && apt-get install -y --force-yes python3"



msg "Sweet!"
msg "The user ${USER} can ssh the remote $SERVER as root and use Fabric"



