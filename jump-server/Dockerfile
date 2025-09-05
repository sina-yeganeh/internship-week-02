FROM ubuntu:24.04

# Update and install openssh configure SSH demon
RUN sudo apt update && \
    sudo apt install -y openssh-server && \
    sudo mkdir /var/run/sshd

# Create a user for dev1 and dev2 to prevent them login as root
# set password to "user" and set shell to bash and finally add them
# to "sudo" gropue if root privilage needed
RUN useradd -m -s /bin/bash user && \
    echo "user:user" | chpasswd && \
    usermod -aG sudo user

# Allow passwordless login (for dev2)
RUN mkdir -p /home/user/.ssh && \
    chmod 700 /home/user.

# Copy public key of dev2 as authorized key to container
# COPY ./config/dev2.pub /home/user/.ssh/authorized_keys

# Change ownership
RUN chown -R user:user /home/user/.ssh

# Enable SSH agent forwarding in SSHD config
RUN echo "AllowAgentForwarding yes" >> /etc/ssh/sshd_config && \
    echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config

# Open SSH port
EXPOSE 22

# Start SSH server
CMD [ "/user/sbin/sshd", "-D" ]