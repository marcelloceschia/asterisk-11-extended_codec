# $Id: 300_srtp_receive_no_key_2.py 369517 2012-07-01 17:28:57Z file $
import inc_sip as sip
import inc_sdp as sdp

sdp = \
"""
v=0
o=- 0 0 IN IP4 127.0.0.1
s=tester
c=IN IP4 127.0.0.1
t=0 0
m=audio 4000 RTP/AVP 0 101
a=rtpmap:0 PCMU/8000
a=sendrecv
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15
a=crypto:0 AES_CM_128_HMAC_SHA1_80 inline
"""

args = "--null-audio --auto-answer 200 --max-calls 1 --use-srtp 1 --srtp-secure 0"
include = []
exclude = []

sendto_cfg = sip.SendtoCfg( "caller send crypto attr without key, callee must not accept the call", 
			    pjsua_args=args, sdp=sdp, resp_code=406, 
			    resp_inc=include, resp_exc=exclude)
