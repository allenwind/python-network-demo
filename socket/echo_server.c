#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

#define ECHO_PORT 8080
#define MAX_CLIENT_NUM 10

int main() {
	int sock_fd;
	struct sockaddr_in serv_addr;

	int clientfd;
	struct sockaddr_in clientAdd;

	char buff[101];
	socklen_t len;
	int n;

	sock_fd = socket(AF_INET, SOCK_STREAM, 0);
	if (sock_fd==-1) {
		printf("create socket error!\n");
		return 0;
	} else {
		printf("success to create socket %d\n", sock_fd);
	}

	bzero(&serv_addr, sizeof(serv_addr));
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(ECHO_PORT);
	serv_addr.sin_addr.s_addr = htons(INADDR_ANY);
	bzero(&(serv_addr.sin_zero), 8);

	if (bind(sock_fd, (struct sockaddr*)&serv_addr, sizeof(serv_addr))!=0) {
		printf("bind address fail! %d\n", errno);
		close(sock_fd);
		return 0;
	} else {
		printf("success to bind address!\n");
	}

	if (listen(sock_fd, MAX_CLIENT_NUM)!=0) {
		printf("listen socket error!\n");
		close(sock_fd);
		return 0;
	} else {
		printf("success to listen\n");
	}

	len = sizeof(clientAdd);

	clientfd = accept(sock_fd, (struct sockaddr*)&clientAdd, &len);
	if (clientfd<0) {
		printf("accept() error!\n");
		close(sock_fd);
		return 0;
	}

	len = sizeof(clientAdd);
	clientfd = accept(sock_fd, (struct sockaddr*)&clientAdd, &len);
	if (clientfd<=0) {
		printf("accept() error!\n");
		close(sock_fd);
		return 0;
	}

	while((n = recv(clientfd, buff, 100, 0))>0) {
		buff[n] = '\0';
		printf("number of receive bytes = %d data = %s\n", n, buff);
		fflush(stdout);
		send(clientfd, buff, n, 0);
		if (strncmp(buff, "quit", 4) == 0) {
			break;
		}
	}

	close(clientfd);
	close(sock_fd);
	 return 0;
}