FROM alpine:3.22.4

ARG GOROOT=/usr/local/bin
ARG GOPATH=/usr/local/bin/go
ARG GO_VERSION=1.25.9
ARG GOLANGCI_LINT_VERSION=v2.12.2

RUN apk update && apk add --no-cache \
    curl \
    bash \
    python3 \
    jq \
    yq \
    make \
    just \
    docker-cli \
    git \
    tar \
    build-base \
    py3-pip

RUN python3 -m venv /opt/venv

RUN curl -fsSL "https://go.dev/dl/go${GO_VERSION}.linux-amd64.tar.gz" -o tmp/go.tgz \
    && tar -C /usr/local -xzf /tmp/go.tgz \
    && rm /tmp/go.tgz \
    && ln -s /usr/local/go/bin/go /usr/local/bin/go \
    && ln -s /usr/local/go/bin/gofmt /usr/local/bin/gofmt

RUN curl -fsSL "https://raw.githubusercontent.com/golangci/golangci-lint/HEAD/install.sh" \
    | sh -s -- -b /usr/local/bin "${GOLANGCI_LINT_VERSION}"

ENV PATH="/opt/venv/bin:/usr/local/bin:/usr/local/sbin:/usr/bin:/sbin:/bin:${GOROOT}/bin:${GOPATH}/bin:${PATH}"

WORKDIR /workspace

CMD ["/bin/bash"]