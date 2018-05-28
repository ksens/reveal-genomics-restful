# reveal-genomics-restful
REST API for SciDB REVEAL/Genomics API

Shell

```sh
time curl -X GET --header 'Accept: application/json' 'http://localhost:8080/ksens/reveal-genomics-basic/1.0/gene_symbols?gene_symbol=EGFR|KRAS|MYC|XAFDAFADER'
"[{\"gene_symbol_id\":\"0\",\"gene_symbol\":\"EGFR\"},{\"gene_symbol_id\":\"1\",\"gene_symbol\":\"KRAS\"},{\"gene_symbol_id\":\"2\",\"gene_symbol\":\"MYC\"},{\"gene_symbol_id\":\"3\",\"gene_symbol\":\"XAFDAFADER\"}]"

# real	0m0.018s
```

R

```R
library(curl)
t1 = proc.time(); req <- curl_fetch_memory("http://localhost:8080/ksens/reveal-genomics-basic/1.0/gene_symbols?gene_symbol=EGFR|KRAS|MYC|XAFDAFADER"); proc.time()-t1
#    user  system elapsed 
#   0.003   0.001   0.008 

cat(rawToChar(req$content))
# "[{\"gene_symbol_id\":\"0\",\"gene_symbol\":\"EGFR\"},{\"gene_symbol_id\":\"1\",\"gene_symbol\":\"KRAS\"},{\"gene_symbol_id\":\"2\",\"gene_symbol\":\"MYC\"},{\"gene_symbol_id\":\"3\",\"gene_symbol\":\"XAFDAFADER\"}]"

parse_headers(req$headers)
# [1] "HTTP/1.0 200 OK"                     
# [2] "Content-Type: application/json"      
# [3] "Content-Length: 217"                 
# [4] "Server: Werkzeug/0.14.1 Python/3.6.4"
# [5] "Date: Mon, 28 May 2018 15:27:11 GMT" 
```