from flask import Flask, request

import requests

app = Flask(__name__)

@app.route('/')

def Lev():

    email = request.args.get('email')

    url = "https://www-useast1a.tiktok.com/passport/web/email/send_code/"
    headers = {

'Host':'www-useast1a.tiktok.com',
'content-length':'164',
'sec-ch-ua':'"Not.A/Brand";v="8","Chromium";v="114","GoogleChrome";v="114"',
'htc6j8njvn-b':'jx22kj',
'x-tt-passport-ttwid-ticket':'Aahbg98ltOD-x8v_AAfydKeaDNxeY0Fp-ev213AKTNgAQFIkFBFzrjV5p3Amva6j3A==',
'htc6j8njvn-d':'ABaAhIDBCKGFgQGAAYIQgISigaIAwBGAzvpCzi_33wd2_deF_2dlnQAAAAAbNPOeAJplg0Nc0xxGJqKTfIjDK4I',
'user-agent':'Mozilla/5.0(Linux;Android10;K)AppleWebKit/537.36(KHTML,likeGecko)Chrome/114.0.0.0MobileSafari/537.36',
'sec-ch-ua-mobile':'?1',
'htc6j8njvn-z':'q',
'content-type':'application/x-www-form-urlencoded',
'htc6j8njvn-c':'AICrm0SJAQAAhOZuvEiSqcLIcOOxjN2rBC9uzG-wKenM8Mbelnb914X_Z2Wd',
'accept':'application/json,text/javascript',
'x-tt-passport-csrf-token':'b9979edc215fbdda5d126b57562890b0',
'htc6j8njvn-a':'fy16dKiRMnWyiRJJmC5qtGPfJJQ5qa9KZO-ZqPUNAMoXexLS3O_v9-GqkOd1ajToX-mQNnj94xZiZ1ZbNllBQniURJGAKoC=P3UKdx6EQQZPU86EkbCx2yEX-FfyUMZRVxvJ84XNb79YOy3nR=0rgkIZhoRgBNFE8kC-GQv_TSkmbkhgpk4lNwluzMEQ-JGeffNhb6Lg-XWeBq7ViZp75v1Ot5L_t81brKEcTKwyqq1WByKAiKz78SkXlqPdIjCETpw=Z1zlOUcCJg4F7ghP8Du9ye=5R-0POoXbEP059bM8xRLP7C1fjWTUPPuvD9m=l67-5nBUKSUoNXhMCk0L3dDnvI9ugzn5uC54zCJGpSJKW7dWEb-10xAoVYmi2hT0NnWsl8nbcuxBBgT1tLE-zwPeYetbkNLc8e_6jb9A3J46k94GrtfptmbKMCCdKEbi21bZ_0p3moxQCeA_FYg9F6hI6IANjmagdRkRTijOYY4IptkS84p6QRdQS2Cy4qDoMDhJy48VBNeJ4Dd-Bzzr6raSbz2SnKQQIxQFOPBGcUhG2ELXmJ=4t42kfJa=2-RAOvWzh6m5=-1atqANWWC-CDrKc9WDIFI34vsmqFUtCCxquQd840PQpdoUGz24CUmrIpnShDXdmoaxTwpqZqVWMVJczET588k8amkDkXdNI_eqRpUo_ylvaF8fsTh=s9NFzxMJBaeK4=zMc86NCqGA8Cc1qX1X6GY2GxWwqcTbbNcrqk0qIO_vJAsJ18vtAD7-_LUKb_l1YZVCaZ30jnP=4mRf6M3lruUPzfr-Z0K6l92wcodZ8o5SMNj_8a1WwdI=at7kkdxQ2IdPSbKnLe0uYnaFcVfLMAUlIZ8jcmXQxDAWA=2DErTWoIoqQcQApowemudP4Mzc_YoMov5-QPBKpaakf7-0T6dtCZZLlJcibVv8KX0r9GjNuEEAvr72ezJ6ryy9LFLnGJf8i_ZZLvo2-84i7caWuO=y5uK8__oZsa_78kJomMk65tg9aarYu=a07b75G1lxnRku4b_BQS7K8jBRdQbhzR=zBcxrY2xK53oxAT5QY8VfWA9T1TDp3W3jz6PczylKBJkbzAYecWdQgAVPkFeJkkyC9WKuRZZK6e0i24T432ZYjqJy_SU8Uea3AvFm=Y5xqL8s0Q5r6eFVdLZZgxeKoajpfbqcfR5Kx7J_uGB5QnI5g2=z0jodakvlg1OuOYreFOSE0pm9ttf9M=mmBXEBtNnqre58cy-YE6EOlub6Rpobm_XeOgPZvPDj7aSKeZ9o6CDXYaAvMS6Vda7-M5hl93Ws7zLCE9oTOUop8VR=Q9tf1CjXIGBG2B9Xn-nfPYLyCX66xS1661ZLOiyi3y=TEf5JNzjC40Ku8=1wLspSqhXSCtlEENytt9rir=JvfUQmh8NU8dWhY2M8FtExgR9_vcSCoJz0Z5QSQtoP9xoUBqa4rrbvAbSKsmsQjegoajefrwAB_=W1SSxrMSvAmLf=oxhXV_0=7n4rSur0ANFBEn6RcA9QoNwTs0B6te0Q9wtcTiZevY3_R-ydbKZrsb2-Toa61bOemMZ1a0_l7MOgGk2e-NFNQU5k35FuowF=rqLT_3gA2ZGs0vjZjGelrDC8-lp8qPrXyOO6_vyOuh6yPj4P1L-4LDhG3-23y2KGdccPpMLI1AWpmEVPdmz13tclUA1doDVyo1078dAXTcId6IaNdugKktqwp=X_zy4pMhPyoGlJ_Il6su0taRzx7tScDriFNsRxRPzCkeWzOBK-xI30croirgmnjiZBSzbE9171E1It3it=knXiCNSIvdbvCiBu4pERm3CsAufOckyWThF1r=eiRnDXjEsItRN0q851MAQJozYcavWJRJCjK36B5jEpnwjB3WAf10y_e7wO4hmqD-AAFBi_nPEI13UnBKKV=MFtGPLsuoKjv9afD-FytQquv0qnn=kFy3=m6k88o8zi_KDAc7CB44C=GBFQTnowiVGF40inxWRXKLn4ocIcnO=-FpOpI5_jrW8WZMyKLWY2EkBMkILAP-08zqQKjmIwwOREGveCRs0A0eA5rdawLRyUB1W19EVG9-86SOFcdzbZsM90PtMNUlXSQS3v3NiBLA67Zvz062v6TrwWJOEL7D=Nv1r=9Oaq_9dVrGVwyzJu3a-Zc6sB3I9VtzGKrs1sRY9hxabg8UYY3oRdk70EkXWmchyjAZvzgcIyNGyMaIZ0xuJ=1XDXaWg4lyVW7bQXY8ojDVW5h8TlJ=Aa2EnbuV3sAcejFj2_0OuJtiewDlpOMx2PIzh=mF-atVFrZj0s5goxp6O3IUYrJTq0UZuCp2UfyYc1RMeG5r_QXTkTbCsi1=YIUZ2ZuwFwPsl07WRuuJSU2mxnlY7iml_-VNg4zFpQuPLpze_bh-7DcYJ4UdUqJ=dugLPBkZNQqlBUqeiuTsCPSdYCZyqSDglcsS-jqv_FGRYXvmKO8jxjqpM-It9oBNZvAbLuaB7z6SZhOP=h4O0LLkNQPhlno4LPzQYpfMAPfbFNFwgReQTV4cQh0qwSVyYFfCKCO9CmQjeQAok91M-POhSr0nsYRZ8RGvUvvBBEotdljgNxk4oNc3fDoDMQAuYdlEfY88h6dfzD2T2w-jDoXdyZCnoRw6FA2P1OxK1aPRUA38fKUekTiqU6KR4IspsmmInf86-UieF7YaYQ0Bk1-52Zr7Sv6kMy53sF-yjB3tT2QecX4K9o_FXkuGjn_JIJSuae3rFVmoykVPaTuFllugv-cjKZnmyy3KhdboVFFmxvxNzqVjlm1Xr96_2hIO=Qv1d-IlDeazOAS5fo7rFyNJaT1fV55CJ7kIgp1N-2a3tfDTnpMWAX2APnf0UPkAiWyKOy3vo=JzpmkzMdhzPZBMDNbzYx2_lWbImUsSZBi7n5B=5meVJ4emw5EUUUBjzKZzZ5iWwy-8Sql=e7zjPk1PA5RWlgET5o6tXxqNJzE-q=9fqulTdP2yzIDoowngPFQN1a-4floLVlcA83NFViu0BzmD9obS5ZWt5mgfQU16QOyzzgdD_=q6f95cZCzcgEPxY101VcXcR4sjIemaDVmnZr-LvV=2uKiIKR1IP5mX9Vz_=FImmfS=s0GEfTofvo=GE8Bx-jMiGU=PMY=AglMvhc_tQf72g9M6TUPSulA3WcXMGJDcKjmc5-GkY2QhMP3GfRtNisyl2DsEL1rSlMBL0WR=Py2v7gBumumwGwnGYVkSXaNBwuGpcs88FIC=XXMTd6GIEzr8Ohc9wjr6QlBhzJ8_WTDDjO-xZTMncFO50lysLIZMLw4_-uWxlO-OO5TvttbzpcQmY4yY22Wq8AsY9kENfJWO50rCh10ErcjwOLNVBmULIAJiFKiG0AGRa35auDmsXJhDWRf2Ko6iVtDCfPbIlGsnm0vUnE5N5ar0i8jz0lQ=-kd6sVg_cAgqya7ZmPzg8WhxNZbUEGZf48NCtXzuuMcxackXOjqEVV9g2noy2m--8Kb3I0b=QrXMBOZT3W2lm7vWGtSuPrUPQrN5vThES_9efTOPEbTm6ATbeNdVcTz=9FMede_N0qonRzqYXP=qaJYhJ5-=OreJ0zCtkKA8Cx=iNYEW2ey27CmmAA-8PWW2uBCSTIA62JTO=qGvmZTaPOxIK=LVGuqpyapsEQGa8hcXjSBkfsg7dVktySW4iNwPQTV3MSORhSPv19tiGRJ3ntYwGgi-xdrfuIh=k90y_z9JBgLb2=GnG3mt80efcNOPxLngESQazmQTBDnvg6LklpVxLTDGPnXY-mzr0-G78Gx=dGYbDB=bKJhei9YM7Zv0ZadtSOJRDYd_XPtk3ESJJjfLO7auTc3PUaIzjAWZwLGSFdvaFPNDZQtoicmdwftLt6zu8rnvD2e7mUbqy349Tx0Oh9OCwqCdPAVuJk2r521P-zcyZsfmz5ytKpoQd2_IyMPWJg4O7aiDYdig=rp_lOifLswqyPbQ4az7XcegGWMhFtAkxv1ahWjImy5XJTbkAL5h5SS_ZcxC61MXKs_cC3vJAnNp0IhnENAWogCQxMjcJFSNj7v09zSNcf1VKzk2BKtfTpErWJ0MQCn=c6zwzW0F7r1SUJ53JWVD7SfUJboTAKxYaBM2OOBFUZp3oNXA5L1dJx=w5j=y0OTq8=ei3xzsV1=b=MjDGBsY51OCfJAMgW42_Ecwx9vCMu8TY7FhDNlVaq_fzDRQuJYDspD2meutgowX_b=LZRERl4qs4JKOROB71UxDm1K20RLwnLTawDApOZngaZa-QwmWnDYJJxqlSwdoxi2=s1mnR4chQLR=4sdDk6D-jIm5OADktur5uez0PnJl0ghGiQl2YSuA2LAQb4kaU0kJv3Gl50Ns_442Ev-iRKFA1aOWJJ4XnBql1KPskg5jmwcQdE-P9-bCqy-zMm7t1Uy94eq=uZZcnudWWvzTjN7onvnGe920EQ9E2l4g5mDUcmpfFINa6dVfEqL5PiyzIOebTsY4CSONkOcoTF5EWWF-WQeTzkpxM9Yx5SvGrs4_UUJEJA3=j-EoLdiue3RYxZcjk5A6FV2yG7RGdxNf0LjZNhzd2gPfCnMcefTm-nMdcEZU5Nn8RxkuRo1gYnsgDRi00b0KfcSOg71Ly1AhR22cukafEdfRjvAeT8wNCDP0ShMbjEdgwekA_VBuKMOGdt-tz87sPdIWnryNX2VtdaNj2QY4iuyM1o9tuPVG2fzP=zk4zYBmuu6nOKMjaUXANUqMyk9AzSDz_1q7DOS1gQGIMUj0RhTdaD8RWCO1khBuu5mj6sdmqpiF9X2Czt9KFJNhjKkWrS5Ner4bLZj=JVluiKpPFBGzdfDVBPtQzlNiUjnYvtMDXi6AzsTCgeiWF_sr9A75jhpTDwW1svnfi871jzdrgyeMcQeyWh4_vYj5-yAAY3nL-WX_5pl11nt3BS7WTnyyKLaDWP88BxUvvxjMbxpsXOOt8xOnwDWhW6eu0ohlu7Bdea=DZepjd6Pyz4ggJfeaC5_W9vOU=6LDVP85SELT_-SI6NOWLgNGwrirNdGOm4DhfQ5Kxat4VOTfzJR_8UtEmOgkBI0pA_meoXWfzF2-UxKa3n5KheDGG63sMzh9yNM5Ui735IeWgwXOBF5Jjmz51npq9UUelY9SzEJBMmaOEEOMYD-Kg15ckjfW3vBjQEh7r70wNCR96EAliSPV7--cKCk2m8l1BVMUZh06s3JKNRkZalWrEK2O2nWIirjg0hkuLWGOF1nn--b2WlArdet969mqn21DOx-UvA7J43BG49jN=bZGcwtaAX2rIYIj0dMTilPgvJTEC62KDx16v3niMgCDNvpQtTSSINRlEcaKT3raufmfbG--2ORm48iXvYimEvmI9jxQ8IX6V__SxY6KoMfmgDrc0AQ91kZB6vzQcQ2RPMgLhD0yKBviz=Va1fJRkvczXdQwMQhGlA_awfqS_x_IhXWMeoBRRfOmn=CLTYkMz2gl=Vl2WWxn1wro2FF_mwI19ZTmuqWvNC3yrYU-R8-MCPYOrp8eBIwDhDGmwAp0XxFJghv5VsVvg5ZBPubFxgNzhw_3JvPBcNUmIxv1TQ0GW_pwm-jey2',
'htc6j8njvn-f':'A9n4p0SJAQAAyoKwYsSie7-usq7tLrDTBzF9sHNZwZlJ3ktzsb1LAkfQAB2fASXtbR0J-BRAwH9CmjJdQ4dCmg==',
'x-mssdk-info':'7liUYJRkHmGtgRo-TZ.Z.7E74CgUzqLv6dzVWvVLX8CERcXXBBEUWoVLJY8KpXIn-lQzZhddWwNygZJ5yjp3ew9z7R0C3kW2PATmcHOUbBMaoMMDsSKcBXwE7-tIXqF4da-5E7ZmBgC4S9jKqX3GfVoemEvJb0L4fKKsY.D114zBanjfbKdVWvSMOc.18rdCekAYife3R1FOaUPp3vaFpwbPutCOYvq6zsqJVFhy.Z8iWF9-uxHTOlLxPh0jug.Z78Z86rwZ9b-sGcRuoxaDnFgNQUmBsV7Nz7O86eWeHmVHKtRAp1OeF6yPdnR1X2Zu5qB0vJJJZZ0LHmOlUqenauY1XVF5pPSVfHT1dKcXf2-ySYkpKAF06wEQb0-UDQnoElJ5uOGr6Mp-YHmysdIEBT5A81UHH2HPPIA0iekhIeYtPjWagXRLrEXIRRxzXwsaQQMvM.-E7hOjz6Q23C-wJdGRxsA1fOfIL8WTuTPFlJoaRCuupJwdYQuGzDDwTXPR0jkQ3LsGRA5dCmFry3YbOf5rPMS2dzQq-H4qact5dAlKurzFeawl6tIwpEARZ4Y1lNYZAa4XhSB3lzRNB-GSWK2HLSJqy1nEPIJrRcr9ArJTFHyrFiECX4TwxXo5dLibHR8visUtY39hv7MQbsE5rE6tRtl0Yi-DUh.ernVpSO8S74KgfiaRiEXKXT-03CT8-w-s72L5i6PzB1Sr.wsoFL18YIuzZwn7rKXWljyWT6Ujy3gy3AwGdkH1fuXtVPrQ-oX1DqgCBFrClfJJT24Dj5-wA08Es0oJ9Fs7EYlnOZCZ5GFp8qVtAudA3cpMwco6Sr8b.Cep-fWVEg6u8-wAcy7SleTpF52gStR3VQr11VbFyz6WxBVGEh48mja1iMswB2Ekv8aI69yWP9n-ArVDezi-AOpw1lQOzDnliXr2lOK4qbanb-kxt8MAayh7.bJkbywW.c6jYjoAtrNgshC4h1iHnIug94Nu3e75Nl6X0ttV8BCOG9ve7MDnzFYSmu62X-3GZ4Q20jM-1TQgrcEi2ijG-LHQ0Lzf7SbZnNRRtydfCC8ab0NheAdBCNcYYWpPz4QAjPldA2tnVOyCrwN1jRr6skTa3-0fBUsMiGeuBeC4.Y3zaM7IC9dIiLwyIVx3SKSep70T5ggPHENrRf1brSGV8Evr-ab9oMHGK9jOptvQXBDOavqgdPJf6sWAYT5W81doF6ScRHlfKS5Vk.udPWaAemT165QL7bjO.gOlin0UByjX09WWQTzaxYv5TKyt3.Q7EJXs5wE-3m4ybOwR6cyr3Mhw5Q3zEavu3ieg76l-5oZiJIG08RxjSCbBZPsXW7IRJaZhxSW2RxbUZyO974vssH5mNM8vsJQPvqrkQncI-w14ZHxJ3gAMYjnRozUnxfWt1shlxmC2ndCreIJckAbMQJZ.O3vNnvDxTVPR7bAdAxsNu6Iv2cyl7L1a8.BfvuhXNX-b3C4I5CEb5q9NHuNZd8hrEPRZ8ZcwSCHtYXvHF3oR0iQML-CgXuQ-JyA4LzI0llK4sRNb7I2OdXuL8p4p8HPOVQpNtqHalKhwWepjlezVoOky7iGH9wlAmgxkVBS3Yn1Gt.4KAaTxXQyjD4ficmQtZWPXuXdW-hw2vmANdhAYKBosJR8h2uOttvLeeJwsU7V8yxAbl.WYktx-QaDBiVoYbc5J1plAalBBpjr07ujumecvLcShuUERe.j2DPdrdmxTyILql6-chV-NMF57PO6Q175q5hHeBDA1KbOmfm2hQxoMnTm9XMxJXdrskva1vosrMK6XT4hmjHOtr84AeWGv9H4IZVFd24e7zgN19BY5C.lXIGtGgph4bZW1qrIIQHTk-qXPL8-qPH33gSRSdnpqbMFW4lnpn5aBcNhVm0Esc3NUO7SAju..8lNzvxrGWjT3Xg-HL5g9LcTlWhuyoqGfgAD6OMHPm.9yGYcESYEFfxK69Up52eUuxM6yr1vIY5uvZC.pQjmC13cfbuOvLJNs9.v7q1gkMxi7I9j9BpqPrN-wn2dM8DUyA5NNFJrn3ewXABx5FRxjtX-nIjWZPWdgTOFpqDta9O9UpyjmUvAE66WKg23d7LMiLAlA9EMr60oJki6arAn-yq-BcA.X6kQBFJfXGw56PLRWILHGvNjm3nh.H8QSuhNS8zafxIrSknyJt4v5mQBJ-pwmF40ltc.w1gLxnO.-rOcSAvelO3cdICd.mgwaoqXZJZTvvRsNtp5x.K9RpPvKdSE2Oy1OYQ.TsnrjyqcEJxH1D4ZMK9kf3PbSFwQfwLWw4AKajTxyqpcqzxr6Ajcupva81xYcAYzgA6v1QLA8VuMAqLj9yPry1bsjN4YQlM0EU6rGmJA2mYUel5mpIjz3yM4wZGjjqz8mXT7JXcHitKtwhnmqryQ9KEJJcWY-bcDDlcsEGSqASYRCbGRRL4.-mASJ5uygc8VQ-iA7EePFdrUcnouIMrtlBp-wqp-qwLKQim3-K3uyuMQa9n5mZt4Vp9ZpGRZgxGIS9T8vjmN1C8Z.4tWoIpDlUDC4hRmvV8FsSWeBBU9BryUaojP.m-0b0SNQDibLcka9h07wKuATsjyYVMmB59SJ74BwKRGZcfysH7d7qJVkDTOf1qer-d-g8WjyU2YqV2tRnSOoJfjs2EEuNiQip.RqsjaxSI6HAQf-2rWeWoFiJxc0GzR.2-hbxGdBko8b76MHSmp1ex62v8zUoe9qO.3eC9OLlB1rluly4BefrWlMk8HhEamFC02kIGmiOQUQhOAtIqZewQYYB3JqogffhIUk22cc6xVL4w==',
'sec-ch-ua-platform':'"Android"',
'origin':'https',
'sec-fetch-site':'same-site',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https',
'accept-encoding':'gzip,deflate,br',
'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
'cookie':'_abck=70B400ADEDF2BB3C5B9CF384933541FC~-1~YAAQBrR7XOB+04KEAQAABExKnAiK3Om710l9HuvdekeuV91Nv6vV4NdJwetXzQUzcfuu5UL/2LX3sgI3f8/tE4iMXGmwO5fHNr8S7aqbLhYRKfErKmTI1SNI/bwp7k63vnZpuWIHTsQQS9zc8prcvMzgiV+AF80xBqUcfRE+7qmHhiWXG/qSt/o8uM1der3Oz7oo85bh6HVselRE1sPfu+wiNUHxlPw0hV02NhwZVd17+3Eg1i650sVHmsnLcEQ2CuZgcjfkC2URA6FYyWeM+VWKlVId6/WI3673ClArNyMd56ggp6nuiz7Ip2cziPSUnzNwfV341uWYa6m4BmxQAWWmbO/tOj5cRQq6gwxinlRlLnwSQUWc09NlLJP3WKTToPKatoQ48gLBOZk=~-1~-1~-1',
'cookie':'_ttp=2Ppk7ZLy30NkAaJR9X9HK2j6xE7',
'cookie':'passport_csrf_token=b9979edc215fbdda5d126b57562890b0',
'cookie':'passport_csrf_token_default=b9979edc215fbdda5d126b57562890b0','cookie':'tt_csrf_token=SBPlCoIl-86JjBSYTgYulL6J9iHBbmUjpI2E',
'cookie':'ttwid=1%7C3xdE1ftOmEEY6D3xpMEckigF2uMGuJ256yhecMdwtIU%7C1689074011%7C76acb594cc9fe78a6e29070aa3b374461ea8a0e365f813a66cf756a1f8f136c1',
'cookie':'msToken=bQS9rhPYkxEJp3sRfZZ6dAzm2kiNuYKp8yVSmUwuZevi_4S6Q-zmcCqpPdtMqC4aEzkGf5qQxPMudCR7GZanpLHGxeMn0ddX0VDrs45PDuwBpfREdi0n4xw2Cm30wfsq_IY5zg=='}

    data = f"mix_mode=1&email={email}&type=31&aid=1459&is_sso=false&account_sdk_source=web&region=IQ&language=en&email_logic_type=2&fixed_mix_mode=1"

    Levi = requests.post(url,headers=headers,data=data).text

    return(Levi)
