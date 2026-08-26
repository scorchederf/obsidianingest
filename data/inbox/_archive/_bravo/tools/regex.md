



regex(field=details, regex="(?<response>response.*)(?<question>QUESTION.*)(?<answer>ANSWER.*)(?<authority>AUTHORITY.*)(?<additional>ADDITIONAL.*)");


regex(field=@rawstring, regex="(?<accountexpires>Account Expires:.*)")
| accountexpires = "*never*"



# guids
`[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}`
# sids
`S-1-[0-59]-\d{2}-\d{8,10}-\d{8,10}-\d{8,10}-[1-9]\d{3}`