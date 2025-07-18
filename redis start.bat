@echo off

set REDIS_DIR=F:\Redis

if not exist "%REDIS_DIR%\redis-server.exe" (
    echo 错误: 在 %REDIS_DIR% 目录下未找到 redis-server.exe
    echo 请确认 Redis 已正确安装并且路径设置无误。
    goto :eof
)

cd /d "%REDIS_DIR%"

start "Redis Server" cmd /c "redis-server.exe redis.windows.conf"

timeout /t 3 /nobreak

start "Redis Client" cmd /k "redis-cli.exe"

echo Redis 服务器和客户端已成功启动！