FROM golang:1.20

WORKDIR /app

COPY source_code/ .

RUN go mod init messenger && go mod tidy || true

RUN go build -o main .

EXPOSE 3002

CMD ["./main"]
