# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.ssh.insert_key = false

  (1..2).each do |id|
    re_name  = ( "vqfx0" + id.to_s ).to_sym
    config.vm.define re_name do |vqfx|
      vqfx.vm.hostname = "vqfx0#{id}"
      vqfx.vm.box = "vqfx-18.4R1.8-re-virtualbox"
# Do not remove / No VMtools installed
      vqfx.vm.synced_folder ".", "/vagrant", disabled: true
# Management port (em1 / em2)
      vqfx.vm.network "private_network", auto_config: false, nic_type: "82540EM", virtualbox__intnet: "vqfx_internal_#{id}"
      vqfx.vm.network "private_network", auto_config: false, nic_type: "82540EM", virtualbox__intnet: "reserved-bridge"
# Interfaces (em3)
      vqfx.vm.network "private_network", auto_config: false, nic_type: "82540EM", virtualbox__intnet: "b2b"
    end
  end

#  config.vm.provider "virtualbox" do |vb|
#    vb.gui = true
# Use ICH9 for the chipset
#    vb.customize ["modifyvm", :id, "--chipset", "ich9"]
#  end

  config.vm.provision "ansible" do |ansible|
    ansible.compatibility_mode = "2.0"
    ansible.groups = {
      "vqfx10k" => ["vqfx01", "vqfx02"],
      "all:children" => ["vqfx10k"]
    }
    ansible.playbook = "ansible_provisioning.yml"
    ansible.extra_vars = { ansible_python_interpreter:"/usr/local/bin/python3" }
  end

end
