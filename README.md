Role bacula_director
====================

Installation and configuration of the Bacula Director.

Role Variables
--------------

[variables](https://github.com/sedovandrew/ansible-role-bacula-director/blob/master/defaults/main.yml)

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: sedovandrew.bacula_director
           become: true
           bacula_director_name: BaculaDirectorName
           bacula_director_console_password: "PASSWORD"
           bacula_director_storages:
             - name: FileServerStorage
               address: storage_server_address
               port: 9103
               password: "storage_server_password"
               device: FileServerDevice
               media_type: File
           bacula_director_file_sets:
             - name: etc
               includes:
                 - options:
                     signature: MD5
                   files:
                     - /etc
           bacula_director_pools:
             - name: File
               comment: File Pool definition
               pool_type: Backup
               recycle: "yes"
               auto_prune: "yes"
               volume_retention: 365 days
               maximum_volume_bytes: 50G
               maximum_volumes: 100
               label_format: "file-"
           bacula_director_jobs:
             - name: EtcFullDailyOnClientJob
               type: Backup
               file_set: etc
               pool: File
               storage: FileServerStorage
               client: FirstClient
               level: Full
               schedule: DailyCycle
               messages: Standard
           bacula_director_schedules:
             - name: DailyCycle
               run:
                 - "daily at 3:17"
           bacula_director_clients:
             - name: FirstClient
               address: first_client_address
               port: 9102
               password: first_client_password
               catalog: MyCatalog

Testing
-------

    molecule test

License
-------

BSD

Author Information
------------------

Sedov Andrey - sedoy80@gmail.com
