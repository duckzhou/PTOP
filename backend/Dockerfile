FROM python:3.11-slim

WORKDIR /app

# 安装 uv
RUN pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

# 复制项目文件
COPY pyproject.toml ../

# 使用 uv 安装依赖（国内镜像源）
RUN cd .. && uv pip install --system -e .

# 复制应用代码
COPY backend/app ./app/

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
