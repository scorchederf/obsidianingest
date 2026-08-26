
# search for user records
```
( user.src eq 'bluecare\gkaur1' )
```
![Alt text](../media/palopanorama/image.png)

# not equal to
```
 ( user.src neq '' ) and ( device_name eq UCQ-DC2-FW-INT-P005 )
```


# search by ip address
`( addr.src in '10.0.10.30' )`