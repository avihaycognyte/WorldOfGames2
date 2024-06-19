docker run \
  --name jenkins \
  --detach \
  --restart=on-failure \
  --env JAVA_OPTS="-Dhudson.plugins.git.GitSCM.ALLOW_LOCAL_CHECKOUT=true" \
  --publish 8080:8080 \
  --publish 50000:50000 \
  --volume //var/run/docker.sock:/var/run/docker.sock \
  myjenkins:1.0