***
[[REST API Design]]
Special values:
1. chi - router similar to net/http
2. 

To know:
1. Implementation of each part:
	1. Configuration package 
	2. Environment file
```go
package config

import (
	"log"
	"os"
	"time"

	"github.com/ilyakaznacheev/cleanenv"
)

type Config struct {
	Env          string `yaml:"env" env:"ENV" envDefault:"local"`
	Storage_path string `yaml:"storage_path" env-required:"true"`
	HTTPServer   `yaml:"http_server"`
}

type HTTPServer struct {
	Address      string        `yaml:"address" env-dafault:"localhost:8888"`
	Time         time.Duration `yaml:"timeout" env_default:"4s"`
	Idle_timeout time.Duration `yaml:"idle_timeout" env_default:"60s"`
}

func MustLoad() *Config {
	configPath := os.Getenv("CONFIG_PATH")
	if configPath == "" {
		log.Fatalf("config file %s\n", configPath)
	}

	if _, err := os.Stat(configPath); os.IsNotExist(err) {
		log.Fatalf("config file does not exist %s\n", configPath)
	}

	var cfg Config

	if err := cleanenv.ReadConfig(configPath, &cfg); err != nil {
		log.Fatalf("cannot read config: %s\n", err)
	}

	return &cfg
}

local.yml

env: "local" # Окружение - local, dev или prod
storage_path: "./storage/storage.db" # файл, в котором будет храниться наша БД
http_server: # конфигурация нашего http-сервера
  address: "localhost:8082"
  timeout: 4s
  idle_timeout: 30s
```

2. Logger in the main file:
```go 
package main

import (
	"log/slog"
	"os"
	"url-shortener/internal/config"
)

const (
	envLocal = "local"
	envDev = "dev"
	envProd = "prod" 
)

func main() {
	cfg := config.MustLoad()
	
	log := Logger(cfg.Env)
	log = log.With(slog.String("env", cfg.Env))

	log.Info("initialize server", slog.String("address", cfg.Address))
	log.Debug("logger debug mode enabled")
}

func Logger(env string) *slog.Logger {
	var log *slog.Logger 

	switch env{
// we enable different layers of logging 
case envLocal:
        log = slog.New(slog.NewTextHandler(os.Stdout, &slog.HandlerOptions{Level: slog.LevelDebug}))
    case envDev:
        log = slog.New(slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{Level: slog.LevelDebug}))
    case envProd:
        log = slog.New(slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{Level: slog.LevelInfo}))
	}
	return log
}
```