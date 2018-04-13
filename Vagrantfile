Vagrant.configure(2) do |config|
  config.vm.define 'scrayping-lecture'
  config.vm.box = 'ubuntu/xenial64'
  config.vm.provider :virtualbox do |v|
    v.cpus   = 2
    v.memory = 2048
  end

  config.vm.network :forwarded_port, host: 8888, guest: 8000

  config.vm.provision 'shell', inline: <<-EOS
    sudo apt-get update
    sudo apt-get upgrade -y
    sudo apt-get install -y build-essential python-dev python3-dev python-pip python3-pip libncursesw5-dev libgdbm-dev libc6-dev zlib1g-dev libsqlite3-dev tk-dev libssl-dev openssl libbz2-dev libreadline-dev git
    git clone https://github.com/kazu0716/scrayping-lecture.git
    cd scrayping-lecture/victim_apps/
    sudo -H pip3 install -r requirements.txt

  EOS
end
