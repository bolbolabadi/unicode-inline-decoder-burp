# -*- coding: utf-8 -*-
from burp import IBurpExtender, IHttpListener

class BurpExtender(IBurpExtender, IHttpListener):

    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Unicode Inline Decoder (Safe JSON)")

        callbacks.registerHttpListener(self)

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        try:
            if not messageIsRequest:  # Only work on responses
                response = messageInfo.getResponse()
                if response:
                    analyzed = self._helpers.analyzeResponse(response)
                    headers = analyzed.getHeaders()

                    # Only process if Content-Type is JSON
                    is_json = any("application/json" in h.lower() for h in headers)
                    if not is_json:
                        return

                    body = response[analyzed.getBodyOffset():].tostring()

                    # Only decode if the body contains "\u"
                    if "\\u" in body:
                        decoded_body = self._decode_unicode(body)
                        new_response = self._helpers.buildHttpMessage(
                            headers, decoded_body.encode("utf-8")
                        )
                        messageInfo.setResponse(new_response)
        except Exception as e:
            print("[Unicode Decoder Error]", e)

    def _decode_unicode(self, data):
        try:
            return data.encode("utf-8").decode("unicode_escape")
        except Exception:
            return data
