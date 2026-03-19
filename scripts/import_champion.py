from models.champions_models import Champion
from services import champions_service
from dotenv import load_dotenv
import os
import httpx
import asyncio
from sqlalchemy.orm import Session
from scripts.get_version import lastest_version

load_dotenv(override=True)

# EXEMPLO FULL_IMAGE
# https://ddragon.leagueoflegends.com/cdn/16.4.1/img/champion/AurelionSol.png

async def import_champions(db: Session):
    try:
        version=os.getenv("GAME_VERSION")
        if not version:
            version= await lastest_version()
        DATA_DRAGON_URL=f'https://ddragon.leagueoflegends.com/cdn/{version}/data/{os.getenv("LANGUAGE", "pt_BR")}/champion.json'    
        async with httpx.AsyncClient() as client:
            response=await client.get(DATA_DRAGON_URL)
            if response.status_code==200:
                data=response.json()
                champ_dict=data['data']

                for champ_key in champ_dict:
                    champ_data=champ_dict[champ_key]

                    champion=Champion(
                        id=int(champ_data['key']),
                        name=champ_data['name'],
                        title=champ_data['title'],
                        image_full=champ_data['image']['full'])
                    
                    champions_service.create_champion_service(db, champion)
                db.commit()
    except Exception:
        db.rollback()
        raise


if __name__ == "__main__":
    asyncio.run(import_champions())