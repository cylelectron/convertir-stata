import pyreadstat

# Cargar el archivo DTA desde el repositorio
df, meta = pyreadstat.read_dta('255LOCIN.DTA')

# Guardar el archivo convertido
df.to_stata('255LOCIN_converted.dta', version=117)

