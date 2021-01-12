# Generated by Django 3.1.4 on 2021-01-11 16:08

from django.db import migrations

from django.core.management.sql import emit_post_migrate_signal


def get_permissions(Permission, perm_list):
    """This function gets Permission objects from a codename list
        :param Permission: Permission object
        :param perm_list: list of codenames
        :return perm_obj_list: [<Permission object()>, ...]
    """
    perm_obj_list = list()
    for perm in perm_list:
        try:
            perm_obj = Permission.objects.get(codename=perm)
            perm_obj_list.append(perm_obj)
        except Permission.DoesNotExist:
            print("perm : ", perm, " DoesNotExist")
    return perm_obj_list


def make_groups(apps, schema_editor):
    """This function creates groups with their permissions"""
    base = [
        "view_article_public"
    ]
    base_p = base + [
        "add_article", "add_anonymous_article",
        "view_article", "del_user_articles",
        "change_user_articles", "add_comment",
        "edit_comment", "del_user_comment"
    ]

    base_pp = base_p + [
        "view_category_forum", "view_category_all_wo_c_f"
    ]

    conseillers = base_p + [
        "view_category_all"
    ]

    experts = base + [
        "view_category_all_wo_c_f",
    ]
    admin = base_pp + conseillers + [
        "del_users_articles", "change_users_articles", "add_category",
        "edit_category", "change_category", "del_category",
        "del_users_comment"
    ]

    groups = [
        {"name": "Admin", "permissions": admin},
        {"name": "Conseiller", "permissions": conseillers},
        {"name": "Expert", "permissions": experts},
        {"name": "Auteur", "permissions": base_pp},
        {"name": "Contributeur", "permissions": base_p},
        {"name": "Abonné", "permissions": base}
    ]
    # emit_post_migrate_signal :
    # https://code.djangoproject.com/ticket/23422
    emit_post_migrate_signal(1, False, 'default')
    Permission = apps.get_model('auth', 'Permission')
    Group = apps.get_model('auth', 'Group')
    for group in groups:
        print(f"[*] Creating group '{group['name']}'")
        group_obj = Group.objects.create(name=group['name'])
        perm = get_permissions(Permission, group['permissions'])
        group_obj.permissions.set(perm)
        group_obj.save()
        print(f"[*] Group '{group['name']}' successfully created")


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(make_groups)
    ]