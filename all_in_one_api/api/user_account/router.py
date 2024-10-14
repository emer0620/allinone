import json
from fastapi import APIRouter,Depends,Body
from sqlalchemy.orm import Session
import api.auth as auth
from . import crud,schemas
from api.spims import crud as spim_crud,schemas as spims_schemas
from api.ps import crud as ps_crud,schemas as ps_schemas

user_account_router = APIRouter(
    prefix= '/User_Account',
    tags= ['User Account']
)

@user_account_router.get('/List')
async def user_account_data_list(db:Session=Depends(auth.get_db)):
    return await crud.user_account_list(db)

@user_account_router.get('/Per_ID')
async def user_account_data_per_id(user_id:int,db:Session=Depends(auth.get_db)):
    return await crud.user_account_per_id(db,user_id)

@user_account_router.post('')
async def user_account_add_new(data:str=Body(...),spims_access:str=Body(...),ps_access:str=Body(...),db:Session=Depends(auth.get_db),sdb:Session=Depends(auth.get_db_spims),pdb:Session=Depends(auth.get_db_ps)):
    data = json.loads(data)
    spims_access = json.loads(spims_access)
    ps_access = json.loads(ps_access)
    check_account = await crud.user_account_check_hrms_id(db,data['hrms_id'])
    if check_account is None:
        for spims in spims_access:
            await spim_crud.access_role_added(sdb,spims_schemas.spims_access_add(**spims))

        for ps in ps_access:
            await ps_crud.ps_user_access_add(pdb,ps_schemas.user_access_add(**ps))

        await crud.user_account_add_new(db,schemas.user_account_create(**data))
        return{
            'status' : 'New Account Added'
        }
    else:
        return {
            'status' : 'Already Added Account'
        }

@user_account_router.post('/Login')
async def user_account_login(data:str=Body(...),db:Session=Depends(auth.get_db)):
    data = json.loads(data)
    return await crud.user_account_login(db,data['username'],data['password'])


@user_account_router.post('/Update')
async def user_account_update(data:str=Body(...),spims_access:str=Body(...),ps_access:str=Body(...),db:Session=Depends(auth.get_db),sdb:Session=Depends(auth.get_db_spims),pdb:Session=Depends(auth.get_db_ps)):
    data = json.loads(data)
    spims_access = json.loads(spims_access)
    ps_access = json.loads(ps_access)
    
    if data['username'] is not None:
        await crud.user_account_username_update(db,data['username'],data['id'])
    if data['password'] is not None:
        await crud.user_account_password_update(db,data['password'],data['id'])

    for spims in spims_access:
        if spims['id'] is not None:
            await spim_crud.access_role_update(sdb,spims_schemas.spims_access_update(**spims),spims['id'])
        else:
            await spim_crud.access_role_added(sdb,spims_schemas.spims_access_add(**spims))
    for ps in ps_access:
        if ps['id'] is not None:
            await ps_crud.ps_user_access_update(pdb,ps_schemas.user_access_update(**ps),ps['id'])
        else:
            await ps_crud.ps_user_access_add(pdb,ps_schemas.user_access_add(**ps))

    return await crud.user_account_update(db,schemas.user_account_update(**data),data['id'])

