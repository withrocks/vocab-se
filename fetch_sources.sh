#!/bin/bash

# Fetch the XML version of the Swedish Kelly list from https://spraakbanken.gu.se/resource/kelly
curl -O https://svn.spraakdata.gu.se/sb-arkiv/pub/lmf/kelly/kelly.xml

# Fetch the XML version of Folkets lexikon from http://folkets-lexikon.csc.kth.se/folkets/om.html
curl -O http://folkets-lexikon.csc.kth.se/folkets/folkets_sv_en_public.xml
