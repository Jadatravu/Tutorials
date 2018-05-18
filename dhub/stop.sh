#!/bin/bash
#kubectl delete deployment fapp dapp 
#kubectl delete service fapp 

kubectl delete deployment fapp dapp ms-mysql-deploy ms-mongo-deploy nodeapp
kubectl delete service fapp ms-mysql ms-mongo nodeapp
