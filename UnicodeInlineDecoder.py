# -*- coding: utf-8 -*-
from burp import IBurpExtender, IHttpListener
import re

class BurpExtender(IBurpExtender, IHttpListener):

    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Unicode Inline Decoder")

        # Register HTTP listener
        callbacks.registerHttpListener(self)

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        try:
            if messageIsRequest:
                request = messageInfo.getRequest()
                if request:
                    decoded = self._decode_unicode(request.tostring())
                    messageInfo.setRequest(decoded.encode("utf-8"))
            else:
                response = messageInfo.getResponse()
                if response:
                    decoded = self._decode_unicode(response.tostring())
                    messageInfo.setResponse(decoded.encode("utf-8"))
        except Exception as e:
            print("[Unicode Decoder Error]", e)

    def _decode_unicode(self, data):
        try:
            # Look for \uXXXX patterns
            if "\\u" in data:
                # Decode escaped Unicode sequences
                return data.encode("utf-8").decode("unicode_escape")
            return data
        except Exception:
            return data
