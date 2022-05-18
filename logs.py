#!/usr/bin/env python3
import logging
import os

# BOILERPLATE
# TODO: usar função
# TODO: user lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("logs.py", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s %(message)s"
)
ch.setFormatter(fmt)
log.addHandler(ch)

# log.debug("Mesagem pro dev, qe, sysadmin")
# log.info("Mensagem geral para usuários")
# log.warning("Aviso que não causa erro")
# log.error("Erro que afeta uma única execução")
# log.critical("Erro geral ex: banco de dados sumiu")

print("---")

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))
