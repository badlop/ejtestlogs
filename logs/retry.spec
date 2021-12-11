{groups,"/home/runner/work/ejabberd/ejabberd/test",ejabberd_SUITE,
        {ldap,[],[{mnesia,[],[{single_user,[],[{offline_single,[]}]}]}]},
        {cases,[offline_feature_enabled,offline_check_identity,
                offline_send_non_existent,offline_view_non_existent,
                offline_remove_non_existent,offline_view_non_integer,
                offline_remove_non_integer,offline_malformed_iq,
                offline_wrong_user,offline_unsupported_iq]}}.
