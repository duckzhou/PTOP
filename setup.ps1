# 使用 uv 初始化项目并安装依赖
Write-Host "=== 使用 uv 初始化 AI Asset Platform ===" -ForegroundColor Green

# 设置国内镜像源
$env:UV_INDEX_URL = "https://pypi.tuna.tsinghua.edu.cn/simple"

# 创建虚拟环境
Write-Host "`n[1/3] 创建虚拟环境..." -ForegroundColor Yellow
uv venv

# 激活虚拟环境
Write-Host "`n[2/3] 激活虚拟环境..." -ForegroundColor Yellow
.\.venv\Scripts\Activate.ps1

# 安装所有依赖（包括开发工具）
Write-Host "`n[3/3] 安装项目依赖（首次安装约需 2-5 分钟）..." -ForegroundColor Yellow
uv pip install -e ".[dev]"

Write-Host "`n✅ 初始化完成！" -ForegroundColor Green
Write-Host "`n下一步：" -ForegroundColor Cyan
Write-Host "1. 启动基础服务：docker-compose up -d" -ForegroundColor White
Write-Host "2. 测试 API: curl http://localhost:8000/health" -ForegroundColor White
Write-Host "3. 查看文档：http://localhost:8000/docs" -ForegroundColor White
