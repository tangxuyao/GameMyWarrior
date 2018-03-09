#!/usr/bin/env bash

go build -a -installsuffix cgo -o gateway ../GatewayService/main.go
go build -a -installsuffix cgo -o crm ../CRMService/main.go