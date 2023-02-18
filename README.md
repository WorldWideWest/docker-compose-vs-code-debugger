# Integration of Docker Compose with VS Code Debugger in Python and Node.js

To run the applications go into the desired folder and run the commands:

To start the application run the command:
```bash
docker-compose -f "docker-compose.debug.yaml" up --build
```

To stop the application Ctrl + C (command + c) and then type the command:
```bash
docker-compose -f "docker-compose.debug.yaml" down
```
