

# python

## reference
- [quickref.me/python](https://quickref.me/python)



## get value enclosed in dbl quotes (eg html attributes)
```py
import re
mydata = '<form name="_ctl0" method="post" action="page.aspx" id="_ctl0"><input type="hidden" name="__VIEWSTATE" value="dDwtNTI0ODU5MDE1Ozs+ZBCF2ryjMpeVgUrY2eTj79HNl4Q=" />'
myvalue = re.findall(r'__VIEWSTATE" value="(.*?)"', mydata)
print(myvalue)

```