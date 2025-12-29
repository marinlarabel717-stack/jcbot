TEXTS = {
    # ===== Main Menu =====
    'main_menu_title': '🏠 Main Menu',
    'main_menu_welcome': '👋 Welcome to Telegram Account Manager Bot!',
    'main_menu_select': 'Please select a function:',
    
    # User info
    'user_info': 'User Information',
    'user_nickname': 'Nickname',
    'user_id': 'ID',
    'user_membership': 'Membership',
    'user_expiry': 'Expiry',
    'status_admin': '👑 Administrator',
    'status_no_member': '❌ No Membership',
    
    # Proxy status
    'proxy_status': 'Proxy Status',
    'proxy_mode': 'Proxy Mode',
    'proxy_mode_enabled': '🟢Enabled',
    'proxy_mode_local': '🔴Local Connection',
    'proxy_count_label': 'Proxy Count',
    'proxy_count_value': '{count} proxies',
    'current_time': 'Current Time',
    
    # Main menu buttons - actual menu items
    'btn_account_check': '🚀 Account Check',
    'btn_format_conversion': '🔄 Format Conversion',
    'btn_change_2fa': '🔐 Modify 2FA',
    'btn_batch_create': '📦 Batch Create',
    'btn_forget_2fa': '🔓 Forgot 2FA',
    'btn_remove_2fa': '❌ Remove 2FA',
    'btn_add_2fa': '➕ Add 2FA',
    'btn_classify_menu': '📦 Account Classification',
    'btn_api_conversion': '🔗 API Conversion',
    'btn_rename_file': '📝 File Rename',
    'btn_merge_account': '🧩 Merge Accounts',
    'btn_cleanup': '🧹 One-Click Cleanup',
    'btn_reauthorize': '🔑 Re-authorize',
    'btn_check_registration': '🕰️ Check Registration Time',
    'btn_profile_update': '📝 Update Profile',
    'btn_check_contact_limit': '🔍 Check Contact Restrictions',
    'btn_vip_menu': '💳 Activate/Redeem Membership',
    'btn_admin_panel': '👑 Admin Panel',
    'btn_proxy_panel': '📡 Proxy Management',
    
    # Language switch
    'btn_language_menu': '🌐 Switch Language',
    'language_menu_title': '🌐 选择语言 / Select Language',
    'language_chinese': '🇨🇳 中文',
    'language_english': '🇬🇧 English',
    'language_switched': '✅ Language switched to English',
    
    # Back button
    'btn_back_to_menu': 'Back to Menu',
    'btn_cancel': '❌ Cancel',
    'btn_confirm': '✅ Confirm',
    
    # Common status
    'status_processing': '⏳ Processing...',
    'status_success': '✅ Success',
    'status_failed': '❌ Failed',
    'status_cancelled': '❌ Cancelled',
    
    # Proxy status
    'proxy_enabled': '🌐 Proxy Mode: Enabled',
    'proxy_disabled': '🌐 Proxy Mode: Disabled',
    'proxy_count': '🌐 Proxy Mode: Enabled ({count} proxies)',
    
    # ===== Account Check =====
    # Upload prompt interface
    'account_check_upload_title': '📨 Please upload your account files',
    'account_check_supported_formats': '📋 Supported formats',
    'account_check_format_zip': '· ZIP archive (recommended)',
    'account_check_format_session': '· Contains Session files (.session)',
    'account_check_format_session_json': '· Contains Session+JSON files (.session + .json)',
    'account_check_format_tdata': '· Contains TData folders',
    'account_check_proxy_enabled': '🌐 Proxy mode: Enabled ({count} proxies)',
    'account_check_proxy_disabled': '🌐 Proxy mode: Disabled',
    'account_check_upload_hint': 'Please select your ZIP file and upload...',
    
    # Start check
    'account_check_starting': '⚡ Starting check for {count} accounts...',
    'account_check_file_type': '📁 File type: {type}',
    'account_check_proxy_mode': '🌐 Proxy mode',
    'account_check_local_mode': '🔴 Local mode',
    'account_check_threads': '⚡ Concurrent threads: {count}',
    'account_check_please_wait': 'Please wait, showing real-time progress...',
    
    # Check progress
    'account_check_in_progress': '⚡ Checking in progress...',
    'account_check_progress_title': '📊 Check Progress',
    'account_check_progress_percent': '· Progress: {percent}% ({done}/{total})',
    'account_check_format': '· Format: {format}',
    'account_check_mode': '· Mode: {mode}',
    'account_check_speed': '· Speed: {speed} accounts/sec',
    'account_check_remaining': '· Est. remaining: {time} min',
    'account_check_proxy_stats': '🔄 Proxy Usage Stats',
    'account_check_proxies_used': '· Proxies used: {count}',
    'account_check_fallback_local': '· Fallback local: {count}',
    'account_check_failed_proxies': '· Failed proxies: {count}',
    'account_check_optimization': '⚡ Optimization Status',
    'account_check_fast_mode': '· Fast mode: {status}',
    'account_check_fast_mode_on': '🟢 On',
    'account_check_fast_mode_off': '🔴 Off',
    'account_check_concurrency': '· Concurrency: {count}',
    'account_check_timeout': '· Check timeout: {seconds}s',
    
    # Account status categories
    'status_no_restriction': 'No Restriction',
    'status_spambot': 'Spambot',
    'status_frozen': 'Frozen',
    'status_banned': 'Banned',
    'status_connection_error': 'Connection Error',
    
    # Result file ZIP naming
    'zip_no_restriction': 'NoRestriction_{count}',
    'zip_spambot': 'Spambot_{count}',
    'zip_frozen': 'Frozen_{count}',
    'zip_banned': 'Banned_{count}',
    'zip_connection_error': 'ConnectionError_{count}',
    
    # File descriptions
    'file_desc_no_restriction': '📦 No Restriction - {count} accounts',
    'file_desc_spambot': '📦 Spambot - {count} accounts',
    'file_desc_frozen': '📦 Frozen - {count} accounts',
    'file_desc_banned': '📦 Banned - {count} accounts',
    'file_desc_connection_error': '📦 Connection Error - {count} accounts',
    
    # Check completion and summary
    'check_time': '⏰ Check time: {time}',
    'check_mode_label': '🌐 Check mode: {mode}',
    'check_mode_proxy': 'Proxy mode',
    'check_mode_local': 'Local mode',
    'all_files_sent': '📤 All files sent successfully!',
    'send_summary': '📊 Send Summary',
    'files_sent_count': '· Successfully sent: {count} files',
    'check_mode_summary': '· Check mode: {mode}',
    'check_duration': '· Check duration: {seconds}s',
    'thanks_message': 'Thanks for using the enhanced bot! To check again, click /start',
    
    # Proxy stats and other statistics
    'total_accounts': 'Total Accounts',
    'proxy_usage_stats': '📡 Proxy Usage Stats',
    'proxies_used_stat': 'Proxies Used',
    'fallback_local_stat': 'Fallback Local',
    'failed_proxies_stat': 'Failed Proxies',
    'local_only_stat': 'Local Only',
    'proxy_connection': '📡 Proxy Connection',
    'local_connection': '🏠 Local Connection',
    'performance_stats': '⚡ Performance Stats',
    'average_speed': 'Average Speed',
    'sending_files': '🚀 Sending classified files, please wait...',
    'processing_file': '📥 Processing your file...',
    'accounts_unit': '',
    'seconds_unit': 's',
    'minutes_unit': 'min',
    'accounts_per_second': 'accounts/s',
}
