class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ips = []

        if 4 < len(s) > 12:
            return ips

        def _valid_section(x):
            if not len(x) or (len(x) > 1 and x[0] == "0") or (int(x) > 255):
                return False
            return True

        for i0 in range(1, 4):
            for i1 in range(1, 4):
                for i2 in range(1, 4):
                    _ip = s[:i0]+'.'+s[i0:i0+i1] + \
                        '.'+s[i0+i1:i0+i1+i2]+'.'+s[i0+i1+i2:]

                    if all(map(_valid_section, _ip.split('.'))):
                        ips.append(_ip)

        return ips
