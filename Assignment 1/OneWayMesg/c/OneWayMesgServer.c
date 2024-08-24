/*
 * Implementation of one-way message server in C
 */


/* include header files for socket related functions */
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <netdb.h>
#include <errno.h>
#include <unistd.h>
#include <stdlib.h>
#include <arpa/inet.h>

/* Maximum message length */
#define MAXMESGLEN  1024


/*
 * Read a message from the socket
 * Put the message in the given buffer
 * Return NULL if nothing to read
 * Otherwise, return the message
 */
char *recvMesg(int sd, char *mesg)
{
  /* Keep reading one char at a time */
  char *ptr = mesg;
  while (1) {
    /* Read one char into the buffer */
    int nread = read(sd, ptr, sizeof(char));

    /* If errors, report and exit */
    if (nread == -1) {
      perror("socket");
      exit(1);
    }

    /* If no byte read, i.e., EOF, return NULL */
    if (nread == 0)
      return(NULL);

    /* If newline character, thats the end of message */
    if (*ptr == '\n') {
      /* string should end with a null character */
      *(ptr+1) = 0;
      break;
    }

    /* Advance the pointer to place the next char */
    ptr++;
  }

  /* Return the message */
  return(mesg);
}


/*
 * The server program starts from here
 */
int main(int argc, char *argv[])
{
  /* Server needs the port number to listen on */
  if (argc != 2) {
    fprintf(stderr, "usage : %s <port>\n", argv[0]);
    exit(1);
  }

  /* Get the port on which server should listen */
  int serverPort = atoi(argv[1]);

  /* Create the server socket */
  int serverSock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
  if (serverSock == -1) {
    perror("socket");
    exit(1);
  }

  /* Bind the socket to the given port */
  struct sockaddr_in serverAddr;
  bzero((char *) &serverAddr, sizeof(serverAddr));
  serverAddr.sin_family = AF_INET;
  serverAddr.sin_addr.s_addr = htonl(INADDR_ANY);
  serverAddr.sin_port = htons(serverPort);
  if (bind(serverSock, (struct sockaddr *) &serverAddr, sizeof(serverAddr)) == -1) {
    perror("bind");
    return(-1);
  }

  /* Set the server for listening */
  listen(serverSock, 5);

  /* Wait to receive a connection request */
  printf("Waiting for a client ...\n");
  struct sockaddr_in clientAddr;
  socklen_t clientAddrLen = sizeof(clientAddr);
  int clientSock = accept(serverSock, (struct sockaddr *) &clientAddr, &clientAddrLen);
  if (clientSock == -1) {
    perror("accept");
    exit(0);
  }

  /* Print the client whereabouts */
  char buffer[MAXMESGLEN];
  inet_ntop( AF_INET, &clientAddr.sin_addr, buffer, sizeof(buffer));
  printf("Connected to a client at ('%s', '%hu')\n", buffer, ntohs(clientAddr.sin_port));

  /* No other clients, close the server socket */
  close(serverSock);

  /* Keep serving the client */
  while (1) {
    /* Wait to receive a message */
    char *message = recvMesg(clientSock, buffer);

    /* if message is NULL ==> client closed connection */
    if (message == NULL) {
      printf("Client closed connection\n");
      close(clientSock);
      break;
    }

    /* Display the message */
    printf("Client: %s", message);
  }
}
