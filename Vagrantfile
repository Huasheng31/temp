# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.ssh.insert_key = false
  config.vm.box = "vqfx-18.4R1.8-re-virtualbox"

  config.vm.define "vqfx01" do |vqfx01|
# Do not remove / No VMtools installed
    vqfx01.vm.synced_folder ".", "/vagrant", disabled: true
    vqfx01.vm.host_name = "vqfx01"
  end

#  config.vm.provider "virtualbox" do |vb|
#    vb.gui = true
# Use ICH9 for the chipset
#    vb.customize ["modifyvm", :id, "--chipset", "ich9"]
#  end

  config.vm.provision "ansible" do |ansible|
    ansible.compatibility_mode = "2.0"
    ansible.groups = {
      "vqfx10k" => ["vqfx01"],
      "all:children" => ["vqfx10k"]
    }
    ansible.playbook = "ansible_provisioning.yml"
    ansible.extra_vars = { ansible_python_interpreter:"/usr/local/bin/python3" }
  end

end
