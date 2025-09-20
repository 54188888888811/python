const zlib = require('pako')
const CryptoJS = require("crypto-js"); // CommonJS
//--通过导入这两个包把原本代码的‘Gt.ZP.’和‘qt’替换
//--使得省却了大量的js代码
//————收获——-->   在遇到某些极其复杂的’方法‘时可以尝试去网上搜索’替代包‘
var e = '362ab6f8de2d4a3f'
        var t = '9mb+Cd82pbkRblrvwJ3l25MXsZRfnXpbgv131s8z+X59ClfZqxwknwW/RtGWHIot0KWj76A2jLD8Pdl/BUAVeJZla4Y8pjiO6edpna5xXWh9pjXUEA5U8lB99bZKg62bYJyYDLjx0DI4Ic/U3pxN5zVcumrZrvxFT52lKP2JvaUZ78XPWUMGduNFO5RWAaRUUfqwEHQuKLzXoju97ggzNf9oQP3Uphy7/KO8nc+493AngzddLEuh3ROQVx33+i/TTMtiobtHVrK0y9A4aTVn/z5PqFlGMmtwN6gLACJ/qufW9Vpx6pJSHSv2qbGZ6BY6rN3F+MJe0RPEUsqXsKxtNkF/MBxmWfiPr5avBkruQbc6zHTomdpouaS+QHs8ZTdSMEZaG5E6x+eB7bZWGih6Dsq/M+pfSwRjgVUlkRXfLlbHJTbb3imamGv/S/4CDGAb/ebupXM58DTQ1TdT6XUmc5m7WhDOMEDJxygbGjngXS4yYX4Tllh6gGf8qpv5e6omA8eANuz3Yoiu3Zq/TVDCIc6O94nFyFkBRVptBgJcOyLqBCnmYOOReeE+rIanmXmgjlu4Gy2RMnBDIbcSbGCtJNmBO5cAt36NfLOrW+cVKWLHI/BzJZ7Y8IPq6hjWfkfx1oPdi2YihbFBNqDanVMwcm7KC/O3+gUquqqvJf55vkf4lBp6iYax6qc0W74DCefzJibG0BVNW3lE1Tp/3SuXvD9u0S4slTN7UicMYC9LtCOTj9LIOmgIUL+DHxniA6K0AfPs1uh+iGiUf+pWrxJTeU6bXD59nrdCaeijHDuM9/5bCW6dW8M6RKKtuJGPelBj+ZhTkSrcVBToEVQ55qLeJBn7nlL5KPppEdpE4OMZtC/uyaLtXaNKTlc6JKbhOSklAl2typF0szMYgklBLtn4m7vcIdzl51nNJ/tsP0ap8HDEC03GaYZccTlj5+qPyBexDu1MJi/dTR1FYPE9Disx2BhJDJTDvBNXBgjGKOax8ceaKfriKVnVfQEHB/QuVyPU4fAdsGXVbmGTb7Ro7Tp9HEvL/T4Qd9xkEHqpEWn/cNwHTwqc8BdXE3hOAX/ISNgFyQbo1miq8eteKAY404sa5OP1OldYxLPxannY1nTTuL4XdsDVqxs2TeotmoidpNsY2fnS8j2v7vQUTH4rb1fUfYzE4GgJa2HVOQQkhAnxPA7P25RmJgJXfi9kZXsNgB9GtUja2o/JuMH+x3U0qWk1cPjZ9bHo7ynQxztUTFmm72iKldqQgmdpLTqABMDb/Hs9Ksr60sDf3rhe9WEQt4l8sd7AY8ofvuZJvnZrzB8x+StiitYA9jke90VohKN1wJFTPzoLs1lDF5g7NkUTl6Tc20WaFGPtBxqOsKdlqaelzJy48iSycIfcc3WbxKIAAU/TSWojwwcbqouS1+ESNXXhTocke5N4TY63ynqSINeAtToGi3/mSt4Jrs37xo5Yny7AGZ7AGPJbC4dotTBA+3LuVr82xm0k8a9Xutug/rftr15M0oyWHirDIEdAim6uNWbKOSPwMTv/8gJaTKM3EKn/bzYKPM44L6bjfLlQlWT/42aVtJhUs6jKn7qMaqmAotKzeU4Jlr7c++X0sQ5nvSatdKAxyGsSX7KMG9D+MlwwXC6th+Aw7A7LmVkweh7sl5vOQJgK21Ujl32NtMMnvAjWQkJ6hINFi1Cicf0kIGfNUvh/TfPj2dD+H5zz0v5OKJQw5b0PEfLKkPFjMnl5yvViD9yid5ZTIPmsNMrBi+Hmqz/5LWiMAsXQ4wvlQiYsjbjl8OX4k5QRgeQ8JIUPujVh7SBvUvXW86Lpryrov+uj7rl9hBhvG2AFc7LZxWKg4jt7so3QzcysugMwloBT9CFV/3yLZ9vILMqI/5pa+WesGUq+N+Z5jhCZS0EdTDHbCs08SXeA8jceaS3WF1hYypNQeWQm8Ataw7+Ui/dmWDhQsC/hBOQl1LqqjUQ50aVHuyGwf+utPOeRbX0hkxEIvhR/Lp939Rde/h5SOCGCeGHOItG4LuImQfyb8//nx3FGk+GeLY3jL9rDIKKnR2TTiVBL1TE5lKZBVBmTYcQVMDTWVbNZnHNxcILHyZ4QkUeIVyfkNdnfLlouTymk5J7ytS6fCk2OxRshJDtEDz8jvlPyZIS2eB7ybFOAKXFNkxYTuSHOVArbuQJVd2CwSNswAFDF4WLMEXiO78YqOohkAZIfdeHObmloc0RuDc7RkA9CNJ4WOYSx2nCTiHvhyLA4GOJcuRyyCUzivZDTm/82ZeWK1e+gqXqH5A1Gtdml8cwopn6jQ8dgzVAa7MXTnwTr0x71+Cb8rl9+aXVLzQB6mg+nU/u8eZYS9MNGM2JmiZbcGCZHeF/FBFdgqf1/G7fMspOi017jwPpzBlqxPfy5S/bILsJNgkR3snR+cX/ZQaWcMlBMc0PvDLbCgaAKoiJ4PviAoMxgM6g/uwt4ll1uU/A0hMV1BctIX2PJeHDrdAMX+j5NYNaRBXjIzqHAu7jlf+7MMGs16WuLWxM5MDRWw3Um2GxBtqPP3vO9HyqSSAOpmvHDSGatwsLjv4rtGqIUinoAr0nvToFMm0HaV2Demmaa5DWQ+qZwcBAoQe09eNnnhe3BPehKImbmHynuopwg6/vWUzadrGxs8dzJj8M8TV6N7gUmtYSfrpztEVAECOJOus7hWRDqzs+CNJucTkElWzDg9clptwB6VoQmpLp6JXTEiRcNg7bqUZh9UDLnnJ5J7zFibCimbawHxRGLqrSjkMSLZRkMDeg6E3/4I6QLggYxfqIah7FxM+F4y0J+3apMWhuBLW+PofgEx67JQhT/j1r001gr09hRxK1lcxjIfZ/d1C5PP2DsNSHfAn4AQnwetbX08FJk8Kr2o2/UiyLmIxPuzsvLhQMrzM8FOgW12kqPL6f9D2piC9/dW1oOpTla6ppIy6V5aLS0fqN37HvhEOOeqINerr9xzUpNCLSKoR0R4VpFugoXowT1Dxq9IkiVCqlH71qmaAndRbVdjv7xEq2EAPQwxX54ZxT5EfRq6dWKhU2MFL5UJLKrTO3oAzZbAAgyjJYAbd9LuxEReJrmHhZaIfG7ZxlOfwQO9Y/cgsHmc6XxfSqi92EKEjtADvGeE4B1pA72Sjr3SFkY5upcDP5QudTMVA9zCshUr/rB2gfEJgq4ousA74LbWz2rU/hohevp3crQxNF+qIE6Q5omc6jcy43/KUrebfqoIqdnHbcoILCtMoeFpuKQSSGtwfoIQGoawJlKNK8sMHrHZ9dHOP7MW7S5MVMEJ3BmHwsc8emIkLNW8uVoUtA3PIK/hoC1oeuF3oJonIiRlfFf6H4rqLgVA+qsIuP3DppB4JeeuQ9zCxah3fGOAjidtwGVedkYPs+gVoZRLlfhd68sOsGn/aibFOuEA5VILVLbuLulc3YNoJsuPwhTvZ4gLaNMBP5KtmfG8jr4i9nWBkw6ZdFeiWvg5EFGADPGZFQEX60WciUf4i8VvtUgpkt1Fcd1kCQql/wpqSN3rSQI13Ji8wMuoR5c7dLGDSERoh3M3d3YZtYYIJWXWD0zza/QX8yNcjmec2SCWgm8qOiu2kKwN8rYFqrGy1WwL2P0rI0Gc+mxiXhqRoRBD0K7hbjjjOSX5bhfmY28f/F7+KMPULO24GscSdtm11arGXirG+n/pZUoUd+0WJ3zNx/aNEKB8vFbVEQJI1BNBB8UDunps7KfZP4WTFGCADJ21S8bw37yg9VgUfVkF9ppuEm8yiCyQ9n8V78PyNy92ElBeTcafCwKos5XYVwWDSPYtRrdVfqAVvCsl6S5WaS7I1dQVW30ZL/dB3Hb2s03HSPaIa/QrPWgwMr3aFtqhb2mpffLwjzKQ8Ym4R9IrXKXpcTMHmEhw7fwuE1LF+O68PcF84FRx1iz8PaWnGTBsD8BByUt3Ui2+xCopk9NU/jToHjOuHiSxWPM6U+9WfC9KLzkiNILDHmH6aYvsYGTHmeWOj7u46bQVEeKsf+YGRnaYZ1RYNg12jU6kKdd0dcuJEpilNMUituQ8q4uicbipwCP3l3ETeXzwtxhtoJe5GxouQRpIMePqtE7DmLXs/Tjosjgu7FV9XQZS0RF9qEU+rceU3DH0i971hefB3guvY98Qt4Gt+qj9rorbZKtfFL/1lo55awmbzLT9Xr86UpsCFxOB1LqPLGJU64v1ilLJwJzZLulVh4gvKLqT6kP661F0LU35zMCjEmdOC/jaH/xVddbFZba6TbB8abW3SrElQGKk77H6VmoMtIcXM1i8d662DCa5DSNfGfOfk6+PycFromYCuIWe8P7Xhq3P5qGwRkhX0LNbJFaW3lCyDssMcg62KBoX8qExkXG4yTIdoimVuhPVmi+bz03DZaed+uPrsE+5gL+jHNXgufJj9vBekvXLeZ2kAIZqKHyAMKXtvRoBqOubBhp74S6giHCTTIybmwx00gZM5MVFpYlLgWxSHsmVHWOKC3sIYgBahlOl3r9wQLK60blZSq3Ql3I7k3wnKcN4iAJiXQReyXQmWYx1ELaSGuq62BxrBsBif/M/bVMatZgKRPfsxqNuArvDoOgF0/9d10Fr9lyLBHdffsyf3+arm65NHzfhNdwf7ssnG2p1iA5N6b7E42iQ6DODXrl0Jr48z70qj39DkrXwA20tJPwmCpfMUzgkL9izVykuFGPPMvjZiuxxCcg/Q1g83KU13B+BEBasicRqdwqGVnCPIBtS0EP3MYcs7aqye7D0zS+1SJTuJ4QmHvaXQPYl2kmuY59aDuarsA807a1gujXS4190NipHDu5jlkjlQ+8vwpT2kuCciss2/qFG5hW35ycmu1lWEiKgNQhWaB34/vpERcFr+raMxsqa+hhusax90AvMZG1aX8FnwtLmZMoqqWUevthCa7X3aNxz5QHq8INM4kiGyj+31ZLfmXajfWwDz+BL3EL5/qof6NAt7Ib/JiNsFfJI1/7CvBbU2O6akhnpPjU9ofubwRiDbYonWXQv0/02bvS4PaS1t7JQ6r6LdvFEMU='
var n = function(t) {
        var e, n = zlib.inflate(new Uint8Array(t.match(/[\da-f]{2}/gi).map((function(t) {
            return parseInt(t, 16)
        }
        )))), r = "", i = 16384;
        for (e = 0; e < n.length / i; e++)
            r += String.fromCharCode.apply(null, n.slice(e * i, (e + 1) * i));
        return r += String.fromCharCode.apply(null, n.slice(e * i)),
        decodeURIComponent(escape(r))
    }(CryptoJS.AES.decrypt(t, CryptoJS.enc.Utf8.parse(e), {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    }).toString(CryptoJS.enc.Hex))
console.log(n)
//——————————————————————原本代码
//var n = function(t) {
//                var e, n = Gt.ZP.inflate(new Uint8Array(t.match(/[\da-f]{2}/gi).map((function(t) {
//                    return parseInt(t, 16)
//                }
//                )))), r = "", i = 16384;
//                for (e = 0; e < n.length / i; e++)
//                    r += String.fromCharCode.apply(null, n.slice(e * i, (e + 1) * i));
//                return r += String.fromCharCode.apply(null, n.slice(e * i)),
//                decodeURIComponent(escape(r))
//            }(qt.AES.decrypt(t, qt.enc.Utf8.parse(e), {
//                mode: qt.mode.ECB,
//                padding: qt.pad.Pkcs7
//            }).toString(qt.enc.Hex));



