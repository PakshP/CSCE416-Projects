/*
 * Implementation of one-way message client in C
 */


/* include header files for socket related functions */
#include <stdio.h>
#include <fcntl.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <time.h>
#include <errno.h>
#include <unistd.h>
#include <stdlib.h>

/* Maximum message length */
#define MAXMESGLEN  1024


/*
 * The client program starts from here
 */
int main(int argc, char *argv[])
{
  /* Client needs server's contact information */
  if (argc != 3) {
    fprintf(stderr, "usage : %s <server name> <server port>\n", argv[0]);
    exit(1);
  }

  /* Get server whereabouts */
  char *serverName = argv[1];
  int serverPort = atoi(argv[2]);


  /* Create a socket */
  int sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
  if (sock == -1) {
    perror("socket");
    exit(1);
  }

  /* Fill the server address structure */
  struct sockaddr_in serverAddr;
  bzero((char *) &serverAddr, sizeof(serverAddr));
  serverAddr.sin_family = AF_INET;
  serverAddr.sin_port = htons(serverPort);

  /* Get the IP address corresponding to server host */
  struct hostent *hostEntry = gethostbyname(serverName);
  if (!hostEntry) {
    perror(serverName);
    exit(1);
  }
  bcopy(hostEntry->h_addr, (char *) &serverAddr.sin_addr, hostEntry->h_length);

  /* Connect to the server */
  if (connect(sock, (struct sockaddr *) &serverAddr, sizeof(serverAddr)) == -1) {
    perror("connect");
    exit(1);
  }
  printf("Connected to server at ('%s', '%d')\n", serverName, serverPort);


  /* Keep reading lines and send to server */
  char buffer[MAXMESGLEN];
  while (1) {
    /* Read a message from the keyboard */
    char *line = fgets(buffer, MAXMESGLEN, stdin);

    /* If EOF, close the connection */
    if (line == NULL) {
      printf("Closing connection\n");
      close(sock);
      break;
    }

    /* Send the line to the server */
    write(sock, line, strlen(line));
  }
}
