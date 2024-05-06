# AWS CLI2とzshを利用するDockerfile
FROM python:3.11

# 必要なパッケージのインストール
RUN apt-get update && apt-get install -y \
    less \
    vim \
    curl \
    unzip \
    sudo \
    git \
    zsh \
    sed \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# AWS CLI v2のインストール
# 公式ドキュメント: https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/install-cliv2-linux.html
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && sudo ./aws/install \
    && rm awscliv2.zip

# デフォルトのシェルをzshに設定
ENV SHELL /usr/bin/zsh
RUN chsh -s /bin/zsh

# zpreztoのインストールと設定
RUN git clone --recursive https://github.com/sorin-ionescu/prezto.git $HOME/.zprezto
SHELL ["/bin/zsh", "-c"]
RUN setopt EXTENDED_GLOB; \
    for rcfile in "${ZDOTDIR:-$HOME}"/.zprezto/runcoms/^README.md(.N); do \
      ln -s "$rcfile" "${ZDOTDIR:-$HOME}/.${rcfile:t}"; \
    done

# zprezto-contribのインストールとプロンプトテーマの設定
RUN git clone --recurse https://github.com/belak/prezto-contrib $HOME/.zprezto/contrib \
    && sed -i "/'prompt'/c \\\ 'contrib-prompt' \\\\\n  'prompt'" /root/.zpreztorc \
    && sed -i "s/theme 'sorin'/theme 'spaceship'/g" /root/.zpreztorc

# Python関連パッケージのインストール
COPY requirements.txt .
RUN pip install -r requirements.txt

# 作業ディレクトリの設定
WORKDIR /app