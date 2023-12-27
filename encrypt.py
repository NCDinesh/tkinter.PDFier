import pikepdf

oldpdf = pikepdf.Pdf.open("farmerriddle.pdf")

no_extr = pikepdf.Permissions(extract=False)

oldpdf.save("newpdf.pdf",
            encryption= pikepdf.Encryption(user="123",
                                           allow=no_extr))