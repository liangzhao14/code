package com.finance.controller;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.finance.config.JwtUtil;
import com.finance.dto.LoginRequest;
import com.finance.dto.LoginResponse;
import com.finance.dto.Result;
import com.finance.entity.User;
import com.finance.mapper.UserMapper;
import lombok.RequiredArgsConstructor;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/auth")
@RequiredArgsConstructor
public class AuthController {

    private final UserMapper userMapper;
    private final PasswordEncoder passwordEncoder;
    private final JwtUtil jwtUtil;

    @PostMapping("/login")
    public Result<LoginResponse> login(@RequestBody LoginRequest request) {
        User user = userMapper.selectOne(
                new LambdaQueryWrapper<User>().eq(User::getUsername, request.getUsername()));
        if (user == null || !passwordEncoder.matches(request.getPassword(), user.getPassword())) {
            return Result.error(401, "用户名或密码错误");
        }
        String token = jwtUtil.generateToken(user.getUsername());
        return Result.ok(new LoginResponse(token, user.getUsername(), user.getAvatar()));
    }

    @PostMapping("/init")
    public Result<String> initUser(@RequestBody LoginRequest request) {
        long count = userMapper.selectCount(null);
        if (count > 0) {
            return Result.error("管理员账号已存在");
        }
        User user = new User();
        user.setUsername(request.getUsername());
        user.setPassword(passwordEncoder.encode(request.getPassword()));
        userMapper.insert(user);
        return Result.ok("初始化成功");
    }
}
