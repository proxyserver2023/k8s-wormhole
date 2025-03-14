FROM golang:1.22 AS builder

WORKDIR /app
COPY go.mod .
COPY go.sum .

RUN go mod download && go mod verify
COPY cmd .
RUN go build -o practice-app cmd/main.go

FROM gcr.io/distroless/base-debian11
COPY --from=builder /app/practice-app /practice-app
ENTRYPOINT [ "/practice-app" ]
