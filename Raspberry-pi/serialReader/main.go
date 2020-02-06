package main

import (
    "github.com/go-redis/redis"
)

var (
    RedisClient *redis.Client
)

func main() {
	RedisClient  =  redis.NewClient(&redis.Options{
		Addr:     Env.Redis.Host + ":" + Env.Redis.Port,
		Password: Env.Redis.Password,
		DB:        Env.Redis.Db,
	})
}