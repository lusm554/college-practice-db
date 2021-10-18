#!/bin/bash
docker-compose -p college-db down
rm -rf pgdata
docker volume prune --force
docker network prune --force
