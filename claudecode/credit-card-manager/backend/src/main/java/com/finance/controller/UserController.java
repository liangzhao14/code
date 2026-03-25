package com.finance.controller;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.finance.dto.Result;
import com.finance.entity.User;
import com.finance.mapper.UserMapper;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Map;
import java.util.Set;
import java.util.UUID;

@RestController
@RequestMapping("/api/user")
@RequiredArgsConstructor
public class UserController {

    private final UserMapper userMapper;

    @Value("${app.upload.avatar-dir:./uploads/avatars}")
    private String avatarDir;

    private static final Set<String> ALLOWED_TYPES = Set.of("image/jpeg", "image/png", "image/gif", "image/webp");
    private static final long MAX_SIZE = 2 * 1024 * 1024; // 2MB

    /**
     * 更新头像为预设头像
     */
    @PutMapping("/avatar")
    public Result<String> updateAvatar(@RequestBody Map<String, String> body) {
        String avatar = body.get("avatar");
        if (avatar == null || !avatar.matches("^preset:[1-6]$")) {
            return Result.error("无效的头像选择");
        }

        User user = getCurrentUser();
        if (user == null) return Result.error(401, "未登录");

        user.setAvatar(avatar);
        userMapper.updateById(user);
        return Result.ok(avatar);
    }

    /**
     * 上传自定义头像
     */
    @PostMapping("/avatar/upload")
    public Result<String> uploadAvatar(@RequestParam("file") MultipartFile file) {
        if (file.isEmpty()) {
            return Result.error("请选择文件");
        }
        if (!ALLOWED_TYPES.contains(file.getContentType())) {
            return Result.error("仅支持 JPG、PNG、GIF、WebP 格式");
        }
        if (file.getSize() > MAX_SIZE) {
            return Result.error("文件大小不能超过 2MB");
        }

        User user = getCurrentUser();
        if (user == null) return Result.error(401, "未登录");

        try {
            Path uploadPath = Paths.get(avatarDir).toAbsolutePath();
            Files.createDirectories(uploadPath);

            // 删除旧的自定义头像
            String oldAvatar = user.getAvatar();
            if (oldAvatar != null && !oldAvatar.startsWith("preset:")) {
                Path oldFile = uploadPath.resolve(oldAvatar);
                Files.deleteIfExists(oldFile);
            }

            String ext = getExtension(file.getOriginalFilename());
            String filename = UUID.randomUUID().toString().replace("-", "") + ext;
            Path target = uploadPath.resolve(filename);
            file.transferTo(target.toFile());

            user.setAvatar(filename);
            userMapper.updateById(user);

            return Result.ok(filename);
        } catch (IOException e) {
            return Result.error("上传失败: " + e.getMessage());
        }
    }

    /**
     * 获取当前用户信息（含头像）
     */
    @GetMapping("/profile")
    public Result<Map<String, Object>> getProfile() {
        User user = getCurrentUser();
        if (user == null) return Result.error(401, "未登录");

        return Result.ok(Map.of(
                "username", user.getUsername(),
                "avatar", user.getAvatar() != null ? user.getAvatar() : "preset:1"
        ));
    }

    private User getCurrentUser() {
        Authentication auth = SecurityContextHolder.getContext().getAuthentication();
        if (auth == null || auth.getPrincipal() == null) return null;
        String username = auth.getPrincipal().toString();
        return userMapper.selectOne(new LambdaQueryWrapper<User>().eq(User::getUsername, username));
    }

    private String getExtension(String filename) {
        if (filename == null) return ".jpg";
        int dot = filename.lastIndexOf('.');
        return dot >= 0 ? filename.substring(dot) : ".jpg";
    }
}
