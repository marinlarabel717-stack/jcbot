TEXTS = {
    # ===== 主菜单 =====
    'main_menu_title': '🏠 主菜单',
    'main_menu_welcome': '👋 欢迎使用 Telegram 账号管理机器人！',
    'main_menu_select': '请选择功能：',
    
    # 用户信息
    'user_info': '用户信息',
    'user_nickname': '昵称',
    'user_id': 'ID',
    'user_membership': '会员',
    'user_expiry': '到期',
    'status_admin': '👑 管理员',
    'status_no_member': '❌ 无会员',
    
    # 代理状态
    'proxy_status': '代理状态',
    'proxy_mode': '代理模式',
    'proxy_mode_enabled': '🟢启用',
    'proxy_mode_local': '🔴本地连接',
    'proxy_count_label': '代理数量',
    'proxy_count_value': '{count}个',
    'current_time': '当前时间',
    
    # 主菜单按钮 - 实际菜单项
    'btn_account_check': '🚀 账号检测',
    'btn_format_conversion': '🔄 格式转换',
    'btn_change_2fa': '🔐 修改2FA',
    'btn_batch_create': '📦 批量创建',
    'btn_forget_2fa': '🔓 忘记2FA',
    'btn_remove_2fa': '❌ 删除2FA',
    'btn_add_2fa': '➕ 添加2FA',
    'btn_classify_menu': '📦 账号拆分',
    'btn_api_conversion': '🔗 API转换',
    'btn_rename_file': '📝 文件重命名',
    'btn_merge_account': '🧩 账户合并',
    'btn_cleanup': '🧹 一键清理',
    'btn_reauthorize': '🔑 重新授权',
    'btn_check_registration': '🕰️ 查询注册时间',
    'btn_profile_update': '📝 修改资料',
    'btn_check_contact_limit': '🔍 检查通讯录限制',
    'btn_vip_menu': '💳 开通/兑换会员',
    'btn_admin_panel': '👑 管理员面板',
    'btn_proxy_panel': '📡 代理管理',
    
    # 语言切换
    'btn_language_menu': '🌐 切换语言',
    'language_menu_title': '🌐 选择语言 / Select Language',
    'language_chinese': '🇨🇳 中文',
    'language_english': '🇬🇧 English',
    'language_switched': '✅ 语言已切换为中文',
    
    # 返回按钮
    'btn_back_to_menu': '返回主菜单',
    'btn_cancel': '❌ 取消',
    'btn_confirm': '✅ 确认',
    
    # 通用状态
    'status_processing': '⏳ 处理中...',
    'status_success': '✅ 成功',
    'status_failed': '❌ 失败',
    'status_cancelled': '❌ 已取消',
    
    # 代理状态
    'proxy_enabled': '🌐 代理模式: 启用',
    'proxy_disabled': '🌐 代理模式: 禁用',
    'proxy_count': '🌐 代理模式: 启用 ({count}个代理)',
    
    # ===== 账号检测 =====
    # 上传提示界面
    'account_check_upload_title': '📨 请上传您的账号文件',
    'account_check_supported_formats': '📋 支持格式',
    'account_check_format_zip': '· ZIP压缩包 (推荐)',
    'account_check_format_session': '· 包含 Session文件 (.session)',
    'account_check_format_session_json': '· 包含 Session+JSON文件 (.session + .json)',
    'account_check_format_tdata': '· 包含 TData 文件夹',
    'account_check_proxy_enabled': '🌐 代理模式: 启用 ({count}个代理)',
    'account_check_proxy_disabled': '🌐 代理模式: 禁用',
    'account_check_upload_hint': '请选择您的ZIP文件并上传...',
    
    # 开始检测
    'account_check_starting': '⚡ 开始检测 {count} 个账号...',
    'account_check_file_type': '📁 文件类型: {type}',
    'account_check_proxy_mode': '🌐 代理模式',
    'account_check_local_mode': '🔴 本地模式',
    'account_check_threads': '⚡ 并发线程: {count}个',
    'account_check_please_wait': '请稍等，实时显示检测进度...',
    
    # 检测进度
    'account_check_in_progress': '⚡ 检测进行中...',
    'account_check_progress_title': '📊 检测进度',
    'account_check_progress_percent': '· 进度: {percent}% ({done}/{total})',
    'account_check_format': '· 格式: {format}',
    'account_check_mode': '· 模式: {mode}',
    'account_check_speed': '· 速度: {speed} 账号/秒',
    'account_check_remaining': '· 预计剩余: {time} 分钟',
    'account_check_proxy_stats': '🔄 代理使用统计',
    'account_check_proxies_used': '· 已使用代理: {count}',
    'account_check_fallback_local': '· 回退本地: {count}',
    'account_check_failed_proxies': '· 失败代理: {count}',
    'account_check_optimization': '⚡ 优化状态',
    'account_check_fast_mode': '· 快速模式: {status}',
    'account_check_fast_mode_on': '🟢 开启',
    'account_check_fast_mode_off': '🔴 关闭',
    'account_check_concurrency': '· 并发数: {count}',
    'account_check_timeout': '· 检测超时: {seconds}秒',
    
    # 账号状态分类
    'status_no_restriction': '🟢 无限制',
    'status_spambot': '🟡 垃圾邮件',
    'status_frozen': '🟡 冻结',
    'status_banned': '🔴 封禁',
    'status_connection_error': '⚫ 连接错误',
    
    # 结果文件ZIP命名
    'zip_no_restriction': '无限制_{count}个',
    'zip_spambot': '垃圾邮件_{count}个',
    'zip_frozen': '冻结_{count}个',
    'zip_banned': '封禁_{count}个',
    'zip_connection_error': '连接错误_{count}个',
    
    # 文件描述
    'file_desc_no_restriction': '📦 无限制 - {count}个账号',
    'file_desc_spambot': '📦 垃圾邮件 - {count}个账号',
    'file_desc_frozen': '📦 冻结 - {count}个账号',
    'file_desc_banned': '📦 封禁 - {count}个账号',
    'file_desc_connection_error': '📦 连接错误 - {count}个账号',
    
    # 检测完成和总结
    'check_time': '⏰ 检测时间: {time}',
    'check_mode_label': '🌐 检测模式: {mode}',
    'check_mode_proxy': '代理模式',
    'check_mode_local': '本地模式',
    'all_files_sent': '📤 所有文件发送完成!',
    'send_summary': '📊 发送总结',
    'files_sent_count': '· 成功发送: {count} 个文件',
    'check_mode_summary': '· 检测模式: {mode}',
    'check_duration': '· 检测时间: {seconds}秒',
    'thanks_message': '感谢使用增强版机器人！如需再次检测，请点击 /start',
}
