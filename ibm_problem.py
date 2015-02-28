import translate
import time

ibm = """
allonza anglicana biz bizon corporat corporata cramberri crips crodana crops crov crupida ctou dana darva dif diga din diptar divka dzecorporata efforta fi fifs fio fivj fotodaps friega gint gip girrin gita giz gizon ibm introndiptaral iof it jidf jo kim kin kison krin kro lap lapta lavanna lina lint lip-trod lon lotran matera mina mipta mit noeir noncabar nonce oioj ol olla pinta pips pra pramsiga primta prin pro prov rita ro rol rontar so srun sui tirin tra transoj tro trondiptar tropditara truna u uinda-pris unita untro uro uronta utro yu
"""

lang_abr_list = """af, ach, ak, am, ar, az, be, bem, bg, bh, bn, br, bs, ca, chr, ckb, co, crs, cs, cy, da, de, ee, el, en, eo, es, es-419, et, eu, fa, fi, fo, fr, fy, ga, gaa, gd, gl, gn, gu, ha, haw, hi, hr, ht, hu, hy, ia, id, ig, is, it, iw, ja, jw, ka, kg, kk, km, kn, ko, kri, ku, ky, la, lg, ln, lo, loz, lt, lua, lv, mfe, mg, mi, mk, ml, mn, mo, mr, ms, mt, ne, nl, nn, no, nso, ny, nyn, oc, om, or, pa, pcm, pl, ps, pt-BR, pt-PT, qu, rm, rn, ro, ru, rw, sd, sh, si, sk, sl, sn, so, sq, sr, sr-ME, st, su, sv, sw, ta, te, tg, th, ti, tk, tl, tn, to, tr, tt, tum, tw, ug, uk, ur, uz, vi, wo, xh, xx-bork, xx-elmer, xx-hacker, xx-klingon, xx-pirate, yi, yo, zh-CN, zh-TW, zu""".replace(" ", "").split(",")

test = "Iof unita cramberri tro fifs, tro gint uro tro mipta friega"

translator = translate.Translator(to_lang="en")
for lang in lang_abr_list:
    translator.from_lang = lang
    print lang
    print translator.translate(test)
    time.sleep(1)

    # for each word in dict
    #for word in ibm.split(' '):
    #    translator.from_lang = lang
    #    print translator.translate(word),
    #    time.sleep(1)